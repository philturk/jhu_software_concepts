## query_data.py
## Be sure to first start my local PostgreSQL server
## Run after load_data.py to query and analyze the data

import psycopg

## Connect to the PostgreSQL database
conn = psycopg.connect(
    dbname="gradcafe_db",
    user="postgres",
    password="DataScience2025!",
    host="localhost",
    port=5432
)

with conn.cursor() as cursor:
    ## 1. Count of Fall 2025 applicants
    cursor.execute("""
        SELECT COUNT(*) FROM applicants
        WHERE term = 'Fall 2025';
    """)
    print("1. Fall 2025 Applicants:", cursor.fetchone()[0])

    ## 2. Percent international students (not 'American' or 'Other'); see note in README.md
    cursor.execute("""
        SELECT ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM applicants), 2)
        FROM applicants
        WHERE us_or_international NOT IN ('American', 'Other');
    """)
    print("2. Percent International Students:", cursor.fetchone()[0], "%")

    ## 3. Average GPA, GRE, GRE_V, GRE_AW analyzed separately with bounds where applicable
    cursor.execute("""
        SELECT ROUND(AVG(gpa)::numeric, 2)
        FROM applicants
        WHERE gpa IS NOT NULL;
    """)
    gpa_avg = cursor.fetchone()[0]

    cursor.execute("""
        SELECT ROUND(AVG(gre)::numeric, 2)
        FROM applicants
        WHERE gre IS NOT NULL AND gre <= 340;
    """)
    gre_avg = cursor.fetchone()[0]

    cursor.execute("""
        SELECT ROUND(AVG(gre_v)::numeric, 2)
        FROM applicants
        WHERE gre_v IS NOT NULL AND gre_v <= 170;
    """)
    gre_v_avg = cursor.fetchone()[0]

    cursor.execute("""
        SELECT ROUND(AVG(gre_aw)::numeric, 2)
        FROM applicants
        WHERE gre_aw IS NOT NULL AND gre_aw <= 6.0;
    """)
    gre_aw_avg = cursor.fetchone()[0]

    print("3. Averages:")
    print("   GPA:", gpa_avg)
    print("   GRE:", gre_avg)
    print("   GRE_V:", gre_v_avg)
    print("   GRE_AW:", gre_aw_avg)

    ## 4. Average GPA of American students in Fall 2025 with max cap
    cursor.execute("""
        SELECT ROUND(AVG(gpa)::numeric, 2)
        FROM applicants
        WHERE term = 'Fall 2025' AND us_or_international = 'American' AND gpa IS NOT NULL AND gpa <= 4.00;
    """)
    print("4. Avg GPA of American students in Fall 2025:", cursor.fetchone()[0])

    ## 5. Percent of Fall 2025 entries that are Acceptances
    cursor.execute("""
        SELECT ROUND(100.0 * COUNT(*) / (
            SELECT COUNT(*) FROM applicants WHERE term = 'Fall 2025'), 2)
        FROM applicants
        WHERE term = 'Fall 2025' AND status ILIKE 'Accepted%';
    """)
    print("5. Percent Acceptances in Fall 2025:", cursor.fetchone()[0], "%")

    ## 6. Average GPA of Fall 2025 Acceptances
    cursor.execute("""
        SELECT ROUND(AVG(gpa)::numeric, 2)
        FROM applicants
        WHERE term = 'Fall 2025' AND status ILIKE 'Accepted%' AND gpa IS NOT NULL;
    """)
    print("6. Avg GPA of Accepted Fall 2025 Applicants:", cursor.fetchone()[0])

    ## 7. Count of Masters applicants to JHU Computer Science
    cursor.execute("""
        SELECT COUNT(*) FROM applicants
        WHERE program ILIKE '%Johns Hopkins University%Computer Science%' AND degree = 'Masters';
    """)
    print("7. JHU CS Masters Applicants:", cursor.fetchone()[0])

conn.close()
