import pandas as pd
import sqlite3
# Connect to database
conn = sqlite3.connect("chinook.db")

# Load tables
customers = pd.read_sql("SELECT * FROM customers", conn)
invoices = pd.read_sql("SELECT * FROM invoices", conn)

# Inner join
cust_invoice = pd.merge(
    customers,
    invoices,
    on="CustomerId",
    how="inner"
)

# Total number of invoices per customer
invoice_count = (
    cust_invoice
    .groupby("CustomerId")
    .size()
    .reset_index(name="Total_Invoices")
)

print(invoice_count.head())

conn.close()
######################################################################
movie = pd.read_csv("movie.csv")

df1 = movie[["director_name", "color"]]
df2 = movie[["director_name", "num_critic_for_reviews"]]

# Left join
left_join = pd.merge(df1, df2, on="director_name", how="left")

# Full outer join
outer_join = pd.merge(df1, df2, on="director_name", how="outer")

print("Left join rows:", left_join.shape[0])
print("Outer join rows:", outer_join.shape[0])
#########################################################################
titanic = pd.read_csv("titanic.csv")

titanic_grouped = (
    titanic
    .groupby("Pclass")
    .agg(
        Avg_Age=("Age", "mean"),
        Total_Fare=("Fare", "sum"),
        Passenger_Count=("PassengerId", "count")
    )
    .reset_index()
)

print(titanic_grouped)
##############################################################################
movie_grouped = (
    movie
    .groupby(["color", "director_name"])
    .agg(
        Total_Critic_Reviews=("num_critic_for_reviews", "sum"),
        Avg_Duration=("duration", "mean")
    )
    .reset_index()
)

print(movie_grouped.head())
#########################################################################
flights = pd.read_csv("flights.csv")

flights_grouped = (
    flights
    .groupby(["Year", "Month"])
    .agg(
        Total_Flights=("FlightNum", "count"),
        Avg_ArrDelay=("ArrDelay", "mean"),
        Max_DepDelay=("DepDelay", "max")
    )
    .reset_index()
)

print(flights_grouped.head())
#############################################################################
def age_group(age):
    if pd.isna(age):
        return "Unknown"
    elif age < 18:
        return "Child"
    else:
        return "Adult"

titanic["Age_Group"] = titanic["Age"].apply(age_group)

print(titanic[["Age", "Age_Group"]].head())
#############################################################################
employee = pd.read_csv("employee.csv")

employee["Normalized_Salary"] = (
    employee
    .groupby("Department")["Salary"]
    .transform(lambda x: (x - x.mean()) / x.std())
)

print(employee.head())
###############################################################################
def movie_length(duration):
    if pd.isna(duration):
        return "Unknown"
    elif duration < 60:
        return "Short"
    elif duration <= 120:
        return "Medium"
    else:
        return "Long"

movie["Length_Category"] = movie["duration"].apply(movie_length)

print(movie[["duration", "Length_Category"]].head())
###############################################################################
titanic_pipeline = (
    titanic
    .pipe(lambda df: df[df["Survived"] == 1])
    .pipe(lambda df: df.assign(Age=df["Age"].fillna(df["Age"].mean())))
    .pipe(lambda df: df.assign(Fare_Per_Age=df["Fare"] / df["Age"]))
)

print(titanic_pipeline.head())
###################################################################################
flights_pipeline = (
    flights
    .pipe(lambda df: df[df["DepDelay"] > 30])
    .pipe(lambda df: df.assign(
        Delay_Per_Hour=df["DepDelay"] / df["AirTime"]
    ))
)

print(flights_pipeline.head())
