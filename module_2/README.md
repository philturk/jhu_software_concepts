Name: Philip Turk; JHED ID pturk1

Module Info: Module 2, Web Scraping, due 2025_06_01

Approach and Notes:

2025_05_30: Confirm the *robot.txt* file permits scraping. See *Screenshot_01.png* and *check.py*.

2025_05_31: Finish building *scrape.py* and pull 10,000 applicant records from [The GradCafe](https://www.thegradcafe.com).

2025_06_01: Finish building *clean.py* and process records into clean JSON file format.

Known Bugs and Gotchas:

2025_05_30: There is a macOS-specific SSL issue that commonly affects Python installations from python.org (particularly Python 3.12 and later). The issue is that Python cannot verify SSL certificates because the system's trusted root certificates aren't available to Python's ssl module by default. Mac users must first run the certificate installation script that comes with their Python distribution before running check.py.

2025_06_01: In the Comments data category for *applicant_data.json*, I made the decision not to initially scrub a few infrequent unicode characters (e.g., u2565) and carriage returns. This can easily be done in any subsequent data analysis.   