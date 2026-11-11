import os
import re
import sqlite3
from datetime import datetime
from zoneinfo import ZoneInfo
from flask import Flask, render_template, request, redirect, url_for, flash, g

APP_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.environ.get("DB_PATH", os.path.join(APP_DIR, "attendance.db"))
app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-this-before-deployment")
CAMPUS_TIMEZONE = ZoneInfo("Africa/Nairobi")

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
        g.db.execute("""
            CREATE TABLE IF NOT EXISTS attendance (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                registration_number TEXT NOT NULL,
                attendance_date TEXT NOT NULL,
                attendance_time TEXT NOT NULL,
                UNIQUE(registration_number, attendance_date)
            )
        """)
        g.db.commit()
    return g.db

@app.teardown_appcontext
def close_db(exception=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/sign-in")
def sign_in():
    reg = request.form.get("registration_number", "").strip().upper()
    # Accept common registration-number characters; adjust this rule to match KMTC's format.
    if not reg or len(reg) > 40 or not re.fullmatch(r"[A-Z0-9/-]+", reg):
        flash("Please enter a valid registration number.", "error")
        return redirect(url_for("index"))

    now = datetime.now(CAMPUS_TIMEZONE)
    day = now.strftime("%Y-%m-%d")
    clock = now.strftime("%H:%M:%S")
    db = get_db()
    try:
        db.execute(
            "INSERT INTO attendance (registration_number, attendance_date, attendance_time) VALUES (?, ?, ?)",
            (reg, day, clock)
        )
        db.commit()
        flash(f"Attendance recorded for {reg} at {now.strftime('%I:%M %p')}.", "success")
    except sqlite3.IntegrityError:
        flash(f"{reg} has already signed in today.", "info")
    return redirect(url_for("index"))

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=False)