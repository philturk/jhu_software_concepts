Name: Philip Turk; JHED ID pturk1

Module Info: Module 02, Web Scraping, due 2025_06_01

Approach and Notes:

2025_05_30: Confirm the *robot.txt* file permits scraping. See *Screenshot_01.pdf* and *check.py*.

Known Bugs and Gotchas:

2025_05_30: There is a macOS-specific SSL issue that commonly affects Python installations from python.org (particularly Python 3.12 and later). The issue is that Python cannot verify SSL certificates because the system's trusted root certificates aren't available to Python's ssl module by default. Mac users must first run the certificate installation script that comes with their Python distribution.