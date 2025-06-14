Name: Philip Turk; JHED ID pturk1

Module Info: Module 3, Databases, due 2025_06_08

Approach and Notes:

2025_06_06: Add *load_data.py* for PostgreSQL database operations after deeper understanding gained from last night's office hour.

2025_06_07: 
- Add *query_data.py* for PostgreSQL data analysis and applicant statistics.
- I note that there is no `Other` value in the `us_or_international` column variable of the applicants database table.
- For Questions 3. and 4. from Part 2 of the assignment, note that bounds were put into place. I discuss this in the written assignment. 

2025_06_08: 
- Add Flask application structure with routes and database connection; include CSS and HTML templates for data analysis display.
- Optional files *applicant_data.json* and *applicants.csv* are added here for organizational purposes.

Known Bugs and Potential Issues:

2025_06_06: I am using a local PostgreSQL server.

2025_06_07: Issues I noted this morning:
- Be careful to spell out Johns Hopkins University for Question 7., Part 2 of the assignment; it is not just 'JHU'.
- For the `program` column variable of the applicants database table, I did *not* turn all text into lowercase.
- In *query_data.py*, beware of a classic PostgreSQL quirk. One needs to cast an average from double precision to numeric before rounding.
 