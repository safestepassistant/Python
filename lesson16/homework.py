# =========================
# Pandas Basics – Homework
# =========================

import pandas as pd
import sqlite3

# -------------------------
# PART 1: Reading Files
# -------------------------

# 1. chinook.db (SQLite)
conn = sqlite3.connect("chinook.db")
customers_df = pd.read_sql("SELECT * FROM customers", conn)
conn.close()

print("Customers table (first 10 rows):")
print(customers_df.head(10))
print("\n")


# 2. iris.json
iris_df = pd.read_json("iris.json")

print("Iris dataset shape:")
print(iris_df.shape)

print("Iris column names:")
print(iris_df.columns)
print("\n")


# 3. titanic.xlsx
titanic_df = pd.read_excel("titanic.xlsx")

print("Titanic dataset (first 5 rows):")
print(titanic_df.head())
print("\n")


# 4. Flights parquet file
flights_df = pd.read_parquet("flights.parquet")

print("Flights dataset info:")
print(flights_df.info())
print("\n")


# 5. movie.csv
movie_df = pd.read_csv("movie.csv")

print("Random sample of 10 movies:")
print(movie_df.sample(10))
print("\n")


# -------------------------
# PART 2: Exploring DataFrames
# -------------------------

# 1. iris.json
# Rename columns to lowercase
iris_df.columns = iris_df.columns.str.lower()

# Select only sepal_length and sepal_width
iris_sepal = iris_df[["sepal_length", "sepal_width"]]

print("Iris sepal columns:")
print(iris_sepal.head())
print("\n")


# 2. titanic.xlsx
# Passengers older than 30
titanic_above_30 = titanic_df[titanic_df["age"] > 30]

print("Passengers older than 30:")
print(titanic_above_30.head())
print("\n")

# Count male and female passengers
print("Gender counts:")
print(titanic_df["sex"].value_counts())
print("\n")


# 3. Flights parquet file
# Select origin, dest, carrier
flights_selected = flights_df[["origin", "dest", "carrier"]]

print("Flights selected columns:")
print(flights_selected.head())
print("\n")

# Number of unique destinations
print("Number of unique destinations:")
print(flights_df["dest"].nunique())
print("\n")


# 4. movie.csv
# Movies longer than 120 minutes
long_movies = movie_df[movie_df["duration"] > 120]

# Sort by director_facebook_likes (descending)
long_movies_sorted = long_movies.sort_values(
    by="director_facebook_likes",
    ascending=False
)

print("Long movies sorted by director Facebook likes:")
print(long_movies_sorted.head())
print("\n")


# -------------------------
# PART 3: Challenges
# -------------------------

# Iris statistics
print("Iris statistics (mean, median, std):")
print(iris_df.describe().loc[["mean", "50%", "std"]])
print("\n")


# Titanic age statistics
print("Titanic age statistics:")
print("Min age:", titanic_df["age"].min())
print("Max age:", titanic_df["age"].max())
print("Sum of ages:", titanic_df["age"].sum())
print("\n")


# Movie.csv
# Director with highest total director_facebook_likes
director_likes = movie_df.groupby("director_name")["director_facebook_likes"].sum()
top_director = director_likes.idxmax()

print("Director with highest total Facebook likes:")
print(top_director)
print("\n")

# 5 longest movies and their directors
longest_movies = movie_df.sort_values("duration", ascending=False)[
    ["movie_title", "duration", "director_name"]
].head(5)

print("5 longest movies:")
print(longest_movies)
print("\n")


# Flights parquet file
# Check missing values
print("Missing values in Flights dataset:")
print(flights_df.isnull().sum())
print("\n")

# Fill missing values in a numerical column with mean
# Example: 'dep_delay' (change if your column name is different)
if "dep_delay" in flights_df.columns:
    flights_df["dep_delay"] = flights_df["dep_delay"].fillna(
        flights_df["dep_delay"].mean()
    )

print("Missing values handled for Flights dataset.")
