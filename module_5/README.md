Name: Philip Turk; JHED ID pturk1

Module Info: Module 5, Code Assurance and Security, due 2025_06_17

Approach and Notes:

2025_06_15: Files that receive a 10/10 via Pylint: 
- *app/__init__.py*, *db.py*

2025_06_08: 
- Add Flask application structure with routes and database connection; include CSS and HTML templates for data analysis display.
- Optional files *applicant_data.json* and *applicants.csv* are added here for organizational purposes.

Known Bugs and Potential Issues:

2025_06_15: I am using a local PostgreSQL server.

2025_06_15: Issues I noted:
- When linting *db.py*, there are two Pylint false positives related to type inference; specifically, "Class 'value' has no 'cursor' / 'close' member". As I came to discover, this usually happens when Pylint cannot infer the type of the object returned by `psycopg.connect()`. Since Pylint doesn’t see the type as `psycopg.Connection`, it just calls it value and warns you that it can't find `cursor()` or `close()`. I easily spent 30 minutes trying various workarounds. A targeted `# pylint: disable=no-member` is the cleanest, most maintainable solution. 