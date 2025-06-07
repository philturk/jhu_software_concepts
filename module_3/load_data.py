## load_data.py
## Be sure to first start my local PostgreSQL server
## Following structure set forth by lecture slides and assigned reading (https://realpython.com/python-sql-libraries/)

import json
import psycopg
from datetime import datetime

## Step 1: Connection function to PostgreSQL server
def create_connection(db_name, db_user, db_password, db_host, db_port):
    try:
        conn = psycopg.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )
        print(f"Connected to database: {db_name}")
        return conn
    except psycopg.OperationalError as e:
        print(f"Connection error: {e}")
        return None

## Step 2: Create a new database
def create_database(conn, new_db_name):
    conn.autocommit = True
    with conn.cursor() as cursor:
        cursor.execute(f"CREATE DATABASE {new_db_name};")
        print(f"Database '{new_db_name}' created successfully.")

## Step 3: Create the applicants table
def create_table(conn):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS applicants (
        p_id SERIAL PRIMARY KEY,
        program TEXT,
        comments TEXT,
        date_added DATE,
        url TEXT,
        status TEXT,
        term TEXT,
        us_or_international TEXT,
        gpa FLOAT,
        gre FLOAT,
        gre_v FLOAT,
        gre_aw FLOAT,
        degree TEXT
    );
    """
    with conn.cursor() as cursor:
        cursor.execute(create_table_query)
        conn.commit()
        print("Table 'applicants' created successfully.")

## Step 4: Load and transform the JSON data
def load_applicants_from_json(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    transformed = []
    for applicant in data:
        program = f"{applicant['School']} {applicant['Program']}"
        comments = applicant.get("Comments", "NA")
        date_added = datetime.strptime(applicant["DateAdded"], "%B %d, %Y").date()
        url = applicant.get("URL", "")
        status = applicant.get("Decision", "")
        term = applicant.get("SemesterYear", "")
        us_or_international = applicant.get("Citizenship", "")
        gpa = float(applicant["GPA"]) if applicant["GPA"] != "NA" else None
        gre = float(applicant["GRE"]) if applicant["GRE"] != "NA" else None
        gre_v = float(applicant["GRE_V"]) if applicant["GRE_V"] != "NA" else None
        gre_aw = float(applicant["GRE_AW"]) if applicant["GRE_AW"] != "NA" else None
        degree = applicant.get("DegreeType", "")

        transformed.append((
            program,
            comments,
            date_added,
            url,
            status,
            term,
            us_or_international,
            gpa,
            gre,
            gre_v,
            gre_aw,
            degree
        ))
    print(f"{len(transformed)} applicants transformed.")
    return transformed

## Step 5: Insert applicants into the database
def insert_applicants(conn, applicants):
    insert_query = """
    INSERT INTO applicants (
        program, comments, date_added, url, status,
        term, us_or_international, gpa, gre, gre_v, gre_aw, degree
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    with conn.cursor() as cursor:
        cursor.executemany(insert_query, applicants)
        conn.commit()
        print(f"{len(applicants)} applicants inserted into the table.")

## Main execution block
if __name__ == "__main__":
    ## Step 0: Configuration
    DB_PARAMS = {
        "db_name": "postgres",
        "db_user": "postgres",
        "db_password": "DataScience2025!",
        "db_host": "localhost",
        "db_port": 5432
    }

    ## Step 1: Connect to default DB and create new DB (optional)
    conn = create_connection(**DB_PARAMS)
    if conn:
        try:
            create_database(conn, "gradcafe_db")
        except psycopg.errors.DuplicateDatabase:
            print("Database already exists, skipping creation.")
        conn.close()

    ## Step 2: Connect to new database and set up table
    DB_PARAMS["db_name"] = "gradcafe_db"
    conn = create_connection(**DB_PARAMS)
    if conn:
        create_table(conn)

        ## Step 3: Load and insert data into the database table
        applicants = load_applicants_from_json("applicant_data.json")
        insert_applicants(conn, applicants)

        conn.close()
