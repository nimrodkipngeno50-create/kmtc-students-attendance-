# KMTC Nairobi Campus Student Attendance System — Render deployment

## Deploy

1. Extract this ZIP.
2. Create a GitHub repository named `kmtc-student-attendance`.
3. Upload the **contents** of the `student_attendance_system` folder to the repository root (so `app.py`, `requirements.txt`, `render.yaml`, `templates/`, and `static/` are at the top level).
4. Sign in to Render and choose **New + → Blueprint**.
5. Connect the GitHub repository and select the branch containing `render.yaml`.
6. Review the Blueprint. It creates a paid Starter web service with a 1 GB persistent disk. Confirm creation/deployment.
7. When deployment finishes, open the `onrender.com` URL shown on the Render service page.
8. Test `/health` (should show `{"status":"ok"}`), then submit a test registration number.

## Important data-storage note

The app is configured to save SQLite data at `/var/data/attendance.db`. The Blueprint attaches a persistent disk at `/var/data`, so attendance records survive app restarts and redeploys. Do not remove the disk or change `DB_PATH` unless you intentionally migrate the database.

## Before collecting real attendance

- Obtain KMTC authorization to collect and store student attendance data.
- The current app accepts any syntactically valid registration number; it does not verify enrollment or identity.
- Arrange access controls for attendance exports and regular backups before using it for official records.
- Render persistent disks are available on paid services; this configuration uses the Starter plan. Check current Render pricing before confirming.

## Local run

`pip install -r requirements.txt`
`python app.py`

The local database defaults to `attendance.db` beside `app.py`.
