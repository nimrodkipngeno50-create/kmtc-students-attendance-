# Student Attendance System — KMTC Nairobi Campus

A small Flask + SQLite student-facing attendance sign-in website.

## What it does
- Students enter their registration number only.
- The server records the date and time using `Africa/Nairobi` time.
- A registration number can only be recorded once per calendar day.
- No student dashboard or admin login is included (student-only access as requested).

## Run it on your computer
1. Install Python 3.10 or newer.
2. Open a terminal in this folder.
3. Create and activate a virtual environment (recommended).
4. Install dependencies:
   `pip install -r requirements.txt`
5. Start the website:
   `python app.py`
6. Open `http://127.0.0.1:5000` in your browser.

The database file `attendance.db` is created automatically in this folder.

## Important before real campus use
- This starter version accepts any correctly formatted registration number. It does not verify that the number belongs to an enrolled KMTC student.
- Registration-number-only sign-in cannot prove who is holding the phone; a student could enter another student's number. For reliable attendance, connect it to an approved student roster and/or add a lecturer-controlled class check-in method.
- The project has no administrator/reporting page because access was set to students only. Attendance records are stored in SQLite on the server.
- Before putting it online, set a long random `SECRET_KEY`, use HTTPS, configure backups, and deploy it on a server that keeps the SQLite database persistent. For multiple app instances or heavier use, use PostgreSQL.
- Confirm that KMTC Nairobi Campus authorizes this system and the handling of student attendance data before collecting real records.
- Adjust the registration-number validation pattern in `app.py` if the campus uses a different format.

## Deploying
This folder is the application source. It is not publicly hosted yet. To make it available to students over the internet, deploy it to a Python hosting provider and share the HTTPS address.