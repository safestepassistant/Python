from bs4 import BeautifulSoup

# 1. Load HTML file
with open("weather.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

# 2. Extract table rows
rows = soup.find("tbody").find_all("tr")

weather_data = []

for row in rows:
    cols = row.find_all("td")
    day = cols[0].text
    temp = int(cols[1].text.replace("°C", ""))
    condition = cols[2].text

    weather_data.append({
        "day": day,
        "temperature": temp,
        "condition": condition
    })

# 3. Display weather data
print("5-Day Weather Forecast:")
for w in weather_data:
    print(f"{w['day']} - {w['temperature']}°C - {w['condition']}")

# 4. Highest temperature
max_temp = max(w["temperature"] for w in weather_data)
hot_days = [w["day"] for w in weather_data if w["temperature"] == max_temp]

print("\nHighest Temperature:")
print(f"{max_temp}°C on {', '.join(hot_days)}")

# 5. Sunny days
sunny_days = [w["day"] for w in weather_data if w["condition"] == "Sunny"]
print("\nSunny Days:")
print(", ".join(sunny_days))

# 6. Average temperature
avg_temp = sum(w["temperature"] for w in weather_data) / len(weather_data)
print(f"\nAverage Temperature: {avg_temp:.2f}°C")




import requests
import sqlite3
import csv
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs"
DB_NAME = "jobs.db"

# 1. Database setup
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    company TEXT,
    location TEXT,
    description TEXT,
    link TEXT,
    UNIQUE(title, company, location)
)
""")

# 2. Scrape website
response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")

jobs = soup.find_all("div", class_="card-content")

for job in jobs:
    title = job.find("h2", class_="title").text.strip()
    company = job.find("h3", class_="company").text.strip()
    location = job.find("p", class_="location").text.strip()
    description = job.find("div", class_="content").text.strip()
    link = job.find("a", text="Apply")["href"]

    # Check if job exists
    cursor.execute("""
    SELECT description, link FROM jobs
    WHERE title=? AND company=? AND location=?
    """, (title, company, location))

    existing = cursor.fetchone()

    if existing:
        if existing[0] != description or existing[1] != link:
            cursor.execute("""
            UPDATE jobs
            SET description=?, link=?
            WHERE title=? AND company=? AND location=?
            """, (description, link, title, company, location))
    else:
        cursor.execute("""
        INSERT INTO jobs (title, company, location, description, link)
        VALUES (?, ?, ?, ?, ?)
        """, (title, company, location, description, link))

conn.commit()

# 3. Filtering function
def filter_jobs(location=None, company=None):
    query = "SELECT title, company, location, link FROM jobs WHERE 1=1"
    params = []

    if location:
        query += " AND location LIKE ?"
        params.append(f"%{location}%")
    if company:
        query += " AND company LIKE ?"
        params.append(f"%{company}%")

    cursor.execute(query, params)
    return cursor.fetchall()

# 4. Export to CSV
def export_to_csv(filename, data):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Company", "Location", "Link"])
        writer.writerows(data)

# Example usage
filtered = filter_jobs(location="Remote")
export_to_csv("filtered_jobs.csv", filtered)

conn.close()
print("Jobs scraped and stored successfully.")




import requests
import json
from bs4 import BeautifulSoup

BASE_URL = "https://www.demoblaze.com/index.html"
API_URL = "https://api.demoblaze.com/bycat"

payload = {"cat": "notebook"}

response = requests.post(API_URL, json=payload)
products = response.json()["Items"]

laptops = []

for p in products:
    laptops.append({
        "name": p["title"],
        "price": f"${p['price']}",
        "description": p["desc"]
    })

# Save to JSON
with open("laptops.json", "w", encoding="utf-8") as f:
    json.dump(laptops, f, indent=4)

print("Laptop data saved to laptops.json")
