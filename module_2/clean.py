# clean.py
# This script reads the HTML file saved by scrape.py, parses the graduate application entries,
# extracts structured data fields, and saves them to a formatted JSON file.

from bs4 import BeautifulSoup
import json
import re

# Load the previously saved HTML file
with open("gradcafe_statistics.html", "r", encoding="utf-8") as f:
    html = f.read()

# Parse HTML content with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
rows = soup.find_all("tr")

entries = []
current_entry = {}

# Iterate through each <tr> in the table
for row in rows:
    tds = row.find_all("td")
    if not tds:
        continue

    # This row contains the main application info
    if len(tds) == 5:
        if current_entry:
            entries.append(current_entry)

        # Initialize a new application entry
        current_entry = {
            "School": "NA",
            "Program": "NA",
            "Comments": "NA",
            "DateAdded": "NA",
            "URL": "NA",
            "Decision": "NA",
            "SemesterYear": "NA",
            "Citizenship": "NA",
            "GRE": "NA",
            "GRE_V": "NA",
            "GRE_AW": "NA",
            "DegreeType": "NA",
            "GPA": "NA"
        }

        # Extract school name
        school_tag = tds[0].find("div", class_="tw-font-medium")
        if school_tag:
            current_entry["School"] = school_tag.get_text(strip=True)

        # Extract program and degree type
        spans = tds[1].find_all("span")
        if spans:
            current_entry["Program"] = spans[0].get_text(strip=True)
        if len(spans) > 1:
            current_entry["DegreeType"] = spans[1].get_text(strip=True)

        # Extract date the entry was added
        current_entry["DateAdded"] = tds[2].get_text(strip=True)

        # Extract admission decision
        decision_tag = tds[3].find("div")
        if decision_tag:
            current_entry["Decision"] = decision_tag.get_text(strip=True)

        # Extract URL link to the applicant entry
        url_tag = tds[4].find("a", href=True)
        if url_tag:
            current_entry["URL"] = "https://www.thegradcafe.com" + url_tag["href"]

    # This row contains additional metadata: semester, GPA, citizenship, GRE scores
    elif tds and tds[0].has_attr("colspan") and tds[0]["colspan"] == "3":
        labels = tds[0].find_all("div", class_="tw-inline-flex")
        for lbl in labels:
            txt = lbl.get_text(strip=True)

            # Match full format: Fall 2025 or Spring 2023
            full_match = re.match(r"(Fall|Spring)\s+(\d{4})", txt)
            if full_match:
                current_entry["SemesterYear"] = f"{full_match.group(1)} {full_match.group(2)}"

            # Match abbreviated format: F18, S22
            abbr_match = re.match(r"\b([FS])(\d{2})\b", txt)
            if abbr_match:
                sem = "Fall" if abbr_match.group(1) == "F" else "Spring"
                year = f"20{abbr_match.group(2)}"
                current_entry["SemesterYear"] = f"{sem} {year}"

            # GPA
            elif "GPA" in txt:
                match = re.search(r"GPA\s+(\d\.\d{1,2})", txt)
                if match:
                    current_entry["GPA"] = match.group(1)

            # Citizenship
            elif txt in ["American", "International"]:
                current_entry["Citizenship"] = txt

            # GRE main score
            elif txt.startswith("GRE V"):
                match = re.search(r"GRE V\s+(\d{2,3})", txt)
                if match:
                    current_entry["GRE_V"] = match.group(1)

            elif txt.startswith("GRE AW"):
                match = re.search(r"GRE AW\s+(\d(?:\.\d{1,2})?)", txt)
                if match:
                    current_entry["GRE_AW"] = match.group(1)

            elif txt.startswith("GRE"):
                match = re.search(r"GRE\s+(\d{2,3})", txt)
                if match:
                    current_entry["GRE"] = match.group(1)

    # This row contains the user's narrative comments
    elif tds and tds[0].has_attr("colspan") and tds[0]["colspan"] == "100%":
        comment = tds[0].get_text(" ", strip=True)
        if comment:
            current_entry["Comments"] = comment

# Append the final entry
if current_entry:
    entries.append(current_entry)

# Save structured data to a JSON file
with open("applicant_data.json", "w", encoding="utf-8") as f:
    json.dump(entries, f, indent=2)

print(f"Saved {len(entries)} applicant entries to applicant_data.json")