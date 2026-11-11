# KMTC Nairobi Campus Student Attendance — Free Render deployment

## Deploy without adding a payment card

1. Extract this ZIP.
2. In your GitHub repository, replace the old project files with the contents of this `student_attendance_system` folder. Keep `app.py`, `requirements.txt`, and `render.yaml` at the repository root, and upload the `templates/` and `static/` folders.
3. Commit the changes to the `main` branch.
4. Return to Render and cancel/close the payment-information dialog. Do not add a card.
5. In the Blueprint setup, use the repository and `main` branch, then choose Retry/refresh so Render reads the updated `render.yaml`.
6. Confirm that the service plan is **Free** and there is no disk or paid database in the configuration. Then apply/deploy.
7. When deployment completes, open the generated `onrender.com` URL and test the homepage and `/health`.

## Critical data warning

This free configuration stores SQLite at `/tmp/attendance.db` on the service's temporary filesystem. Render free services do not provide persistent disks. The database can be lost when the service restarts, spins down, or is redeployed. Free services also spin down after inactivity and may take about a minute to wake up.

Use this only for a demo or trial. Do not use it for official attendance until a persistent database/storage solution and backups are configured. Also, the app accepts registration numbers but does not verify student identity or enrollment.

## Local run

`pip install -r requirements.txt`
`python app.py`
