# =========================
# TASK 1: Library Management System
# =========================

class BookNotFoundException(Exception):
    pass

class BookAlreadyBorrowedException(Exception):
    pass

class MemberLimitExceededException(Exception):
    pass


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False


class Member:
    MAX_BOOKS = 3

    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        self.books[book.title] = book

    def add_member(self, member):
        self.members[member.name] = member

    def borrow_book(self, member_name, book_title):
        if book_title not in self.books:
            raise BookNotFoundException("Book not found")

        book = self.books[book_title]
        member = self.members[member_name]

        if book.is_borrowed:
            raise BookAlreadyBorrowedException("Book already borrowed")

        if len(member.borrowed_books) >= Member.MAX_BOOKS:
            raise MemberLimitExceededException("Borrow limit exceeded")

        book.is_borrowed = True
        member.borrowed_books.append(book_title)

    def return_book(self, member_name, book_title):
        book = self.books[book_title]
        member = self.members[member_name]

        book.is_borrowed = False
        member.borrowed_books.remove(book_title)


# ---- Test Task 1 ----
library = Library()
library.add_book(Book("1984", "George Orwell"))
library.add_book(Book("Python Basics", "Guido"))
library.add_member(Member("Alice"))

library.borrow_book("Alice", "1984")
library.return_book("Alice", "1984")


# =========================
# TASK 2: Student Grades (CSV)
# =========================

import csv

# Create grades.csv
with open("grades.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Subject", "Grade"])
    writer.writerows([
        ["Alice", "Math", 85],
        ["Bob", "Science", 78],
        ["Carol", "Math", 92],
        ["Dave", "History", 74]
    ])

# Read and calculate averages
grades = {}
with open("grades.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        subject = row["Subject"]
        grade = int(row["Grade"])
        grades.setdefault(subject, []).append(grade)

averages = {s: sum(v)/len(v) for s, v in grades.items()}

# Write average_grades.csv
with open("average_grades.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Subject", "Average Grade"])
    for subject, avg in averages.items():
        writer.writerow([subject, avg])


# =========================
# TASK 3: JSON Handling
# =========================

import json

# Create tasks.json
tasks_data = [
    {"id": 1, "task": "Do laundry", "completed": False, "priority": 3},
    {"id": 2, "task": "Buy groceries", "completed": True, "priority": 2},
    {"id": 3, "task": "Finish homework", "completed": False, "priority": 1}
]

with open("tasks.json", "w") as f:
    json.dump(tasks_data, f, indent=4)

# Load tasks
with open("tasks.json", "r") as f:
    tasks = json.load(f)

# Display tasks
for t in tasks:
    print(t["id"], t["task"], t["completed"], t["priority"])

# Task statistics function56euihj20.3_stats(tasks):
    total = len(tasks)
    completed = sum(t["completed"] for t in tasks)
    pending = total - completed
    avg_priority = sum(t["priority"] for t in tasks) / total
    return total, completed, pending, avg_priority

print(task_stats(tasks))

# Save changes (example: mark task 1 completed)
tasks[0]["completed"] = True
with open("tasks.json", "w") as f:
    json.dump(tasks, f, indent=4)

# Convert JSON to CSV
with open("tasks.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["ID", "Task", "Completed", "Priority"])
    for t in tasks:
        writer.writerow([t["id"], t["task"], t["completed"], t["priority"]])
