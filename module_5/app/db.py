"""
This module connects to the PostgreSQL database and retrieves analysis results for the GradCafe 
applicants data. For all intents and purposes, it is the same thing as query_data.py but with a 
little extra functionality to return the results in a structured format for use in the Flask 
application.
"""
import psycopg

def get_analysis_results():
    """Connect to the PostgreSQL database and retrieve analysis results."""
    conn = psycopg.connect(
    dbname="gradcafe_db",
    user="postgres",
    password="DataScience2025!",
    host="localhost",
    port=5432
    )

    results = []

    with conn.cursor() as cursor: # pylint: disable=no-member
        # 1. Count of Fall 2025 applicants
        cursor.execute(
            "SELECT COUNT(*) FROM applicants WHERE term = 'Fall 2025';")
        results.append({
            "question": (
                "How many applicants do you have in your database table who have applied for Fall"
                "2025?"
            ),
            "answer": (
                f"Applicant Count (Fall 2025): {cursor.fetchone()[0]}"
            )
        })

        # 2. Percent international students (not 'American' or 'Other');
        cursor.execute("""
            SELECT ROUND(100.0 * COUNT(*) / (SELECT COUNT(*) FROM applicants), 2)
            FROM applicants
            WHERE us_or_international NOT IN ('American', 'Other');
        """)
        results.append({
            "question": (
                "What percentage of applicants are from international students "
                "(not American or Other)?"
            ),
            "answer": (
                f"Percent International Applicants: {cursor.fetchone()[0]}%"
            )
        })

        # 3. Average GPA, GRE, GRE_V, GRE_AW analyzed separately with bounds where applicable
        cursor.execute(
            "SELECT ROUND(AVG(gpa)::numeric, 2) FROM applicants WHERE gpa IS NOT NULL;")
        gpa = cursor.fetchone()[0]

        cursor.execute(
            (
                "SELECT ROUND(AVG(gre)::numeric, 1) "
                "FROM applicants WHERE gre IS NOT NULL AND gre <= 340;"
            )
        )
        gre = cursor.fetchone()[0]

        cursor.execute(
            (
                "SELECT ROUND(AVG(gre_v)::numeric, 1) "
                "FROM applicants WHERE gre_v IS NOT NULL AND gre_v <= 170;"
            )
        )
        gre_v = cursor.fetchone()[0]

        cursor.execute(
            (
                "SELECT ROUND(AVG(gre_aw)::numeric, 2) "
                "FROM applicants WHERE gre_aw IS NOT NULL AND gre_aw <= 6.0;"
            )
        )
        gre_aw = cursor.fetchone()[0]

        results.append({
            "question": (
                "What is the average GPA, GRE, GRE V, GRE AW of applicants who provided these "
                "metrics?"
            ),
            "answer": (
                f"Average GPA: {gpa}, Average GRE: {gre}, "
                f"Average GRE_V: {gre_v}, Average GRE_AW: {gre_aw}"
            )
        })

        # 4. Average GPA of American students in Fall 2025 with max cap
        cursor.execute("""
            SELECT ROUND(AVG(gpa)::numeric, 2)
            FROM applicants
            WHERE term = 'Fall 2025' AND us_or_international = 'American' AND gpa IS NOT NULL AND gpa <= 4.00;
        """)
        results.append({
            "question": "What is the average GPA of American students in Fall 2025?",
            "answer": f"Average GPA (American, Fall 2025): {cursor.fetchone()[0]}"
        })

        # 5. Percent of Fall 2025 entries that are Acceptances
        cursor.execute("""
            SELECT ROUND(100.0 * COUNT(*) / (
                SELECT COUNT(*) FROM applicants WHERE term = 'Fall 2025'), 2)
            FROM applicants
            WHERE term = 'Fall 2025' AND status ILIKE 'Accepted%';
        """)
        results.append({
            "question": "What percent of applicants for Fall 2025 are Acceptances?",
            "answer": f"Percent Acceptances (Fall 2025): {cursor.fetchone()[0]}%"
        })

        # 6. Average GPA of Fall 2025 Acceptances
        cursor.execute("""
            SELECT ROUND(AVG(gpa)::numeric, 2)
            FROM applicants
            WHERE term = 'Fall 2025' AND status ILIKE 'Accepted%' AND gpa IS NOT NULL;
        """)
        results.append({
            "question": (
                "What is the average GPA of applicants who applied for Fall 2025 and were accepted?"
            ),
            "answer": (
                f"Average GPA (Accepted, Fall 2025): {cursor.fetchone()[0]}"
            )
        })

        # 7. Count of Masters applicants to JHU Computer Science
        cursor.execute("""
            SELECT COUNT(*) FROM applicants
            WHERE program ILIKE '%Johns Hopkins University%Computer Science%' AND degree = 'Masters';
        """)
        results.append({
            "question": (
                "How many entries are from applicants who applied to JHU for a Masters degree in "
                "Computer Science?"
            ),
            "answer": (
                f"JHU Masters Computer Science Applicants Count: {cursor.fetchone()[0]}"
            )
        })

    conn.close() # pylint: disable=no-member
    return results
