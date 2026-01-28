import sqlite3

# =========================
# TASK 1 — ROSTER DATABASE
# =========================

# Connect to roster.db
roster_conn = sqlite3.connect("roster.db")
roster_cursor = roster_conn.cursor()

# 1. Create table
roster_cursor.execute("""
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
""")

# 2. Insert data
roster_cursor.executemany("""
INSERT INTO Roster (Name, Species, Age)
VALUES (?, ?, ?)
""", [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
])

# 3. Update Jadzia Dax to Ezri Dax
roster_cursor.execute("""
UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax'
""")

# 4. Query Bajoran characters
print("Bajoran characters:")
roster_cursor.execute("""
SELECT Name, Age FROM Roster
WHERE Species = 'Bajoran'
""")
for row in roster_cursor.fetchall():
    print(row)

# 5. Delete characters older than 100
roster_cursor.execute("""
DELETE FROM Roster
WHERE Age > 100
""")

# 6. Add Rank column
roster_cursor.execute("""
ALTER TABLE Roster
ADD COLUMN Rank TEXT
""")

# Update ranks
roster_cursor.execute("UPDATE Roster SET Rank = 'Captain' WHERE Name = 'Benjamin Sisko'")
roster_cursor.execute("UPDATE Roster SET Rank = 'Lieutenant' WHERE Name = 'Ezri Dax'")
roster_cursor.execute("UPDATE Roster SET Rank = 'Major' WHERE Name = 'Kira Nerys'")

# 7. Advanced query (Age DESC)
print("\nRoster sorted by Age (DESC):")
roster_cursor.execute("""
SELECT * FROM Roster
ORDER BY Age DESC
""")
for row in roster_cursor.fetchall():
    print(row)

roster_conn.commit()
roster_conn.close()

# =========================
# TASK 2 — LIBRARY DATABASE
# =========================

# Connect to library.db
library_conn = sqlite3.connect("library.db")
library_cursor = library_conn.cursor()

# 1. Create table
library_cursor.execute("""
CREATE TABLE IF NOT EXISTS Books (
    Title TEXT,
    Author TEXT,
    Year_Published INTEGER,
    Genre TEXT
)
""")

# 2. Insert data
library_cursor.executemany("""
INSERT INTO Books (Title, Author, Year_Published, Genre)
VALUES (?, ?, ?, ?)
""", [
    ("To Kill a Mockingbird", "Harper Lee", 1960, "Fiction"),
    ("1984", "George Orwell", 1949, "Dystopian"),
    ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Classic")
])

# 3. Update year for 1984
library_cursor.execute("""
UPDATE Books
SET Year_Published = 1950
WHERE Title = '1984'
""")

# 4. Query Dystopian books
print("\nDystopian books:")
library_cursor.execute("""
SELECT Title, Author FROM Books
WHERE Genre = 'Dystopian'
""")
for row in library_cursor.fetchall():
    print(row)

# 5. Delete books published before 1950
library_cursor.execute("""
DELETE FROM Books
WHERE Year_Published < 1950
""")

# 6. Add Rating column
library_cursor.execute("""
ALTER TABLE Books
ADD COLUMN Rating REAL
""")

# Update ratings
library_cursor.execute("UPDATE Books SET Rating = 4.8 WHERE Title = 'To Kill a Mockingbird'")
library_cursor.execute("UPDATE Books SET Rating = 4.7 WHERE Title = '1984'")
library_cursor.execute("UPDATE Books SET Rating = 4.5 WHERE Title = 'The Great Gatsby'")

# 7. Advanced query (Year ASC)
print("\nBooks sorted by Year Published (ASC):")
library_cursor.execute("""
SELECT * FROM Books
ORDER BY Year_Published ASC
""")
for row in library_cursor.fetchall():
    print(row)

library_conn.commit()
library_conn.close()
