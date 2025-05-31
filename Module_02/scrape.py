# scrape.py
# This script scrapes the HTML pages from The Grad Cafe using urllib3 and saves the combined HTML content.
# It follows pagination to pull in an arbitrary number of applicant entries (e.g., 50 to 10,000).

import urllib3
import time

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Initialize urllib3 pool manager
http = urllib3.PoolManager()

# Base URL for Grad Cafe search results with pagination
base_url = "https://www.thegradcafe.com/survey/?q=Statistics&page={}"  # Page numbers are 1-indexed

# Number of applicant entries to scrape
TARGET_COUNT = 50  # Change this to 10000 when scaling up
entries_per_page = 25  # Grad Cafe typically lists 25 entries per page

# Calculate how many pages we need to visit
page_count = (TARGET_COUNT + entries_per_page - 1) // entries_per_page

# List to store HTML content of all pages
all_html = ""

for page_num in range(1, page_count + 1):
    url = base_url.format(page_num)
    print(f"Fetching page {page_num}: {url}")

    response = http.request('GET', url)
    if response.status == 200:
        all_html += response.data.decode("utf-8")
    else:
        print(f"Failed to retrieve page {page_num}. Status code: {response.status}")

    time.sleep(1)  # Be polite and avoid hammering the server

# Save the combined HTML content to a file
with open("gradcafe_statistics.html", "w", encoding="utf-8") as f:
    f.write(all_html)

print(f"Saved HTML content for {TARGET_COUNT} applicants to gradcafe_statistics.html")