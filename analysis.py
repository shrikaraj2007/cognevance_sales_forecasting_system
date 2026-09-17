
import pandas as pd

# Load sales dataset
df = pd.read_csv("sales_data.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Check missing values
print("Missing Values:")
print(df.isnull().sum())

# Remove duplicate records
df = df.drop_duplicates()

# Sort data by date
df = df.sort_values("Date")

# Monthly Sales
print("\nMonthly Sales:")
print(df[["Date", "Sales"]])

# Yearly Sales
df["Year"] = df["Date"].dt.year
yearly_sales = df.groupby("Year")["Sales"].sum()

print("\nYearly Sales:")
print(yearly_sales)

# Basic statistics
print("\nSales Statistics:")
print(df["Sales"].describe())

# Highest monthly sales
highest_sales = df["Sales"].max()
highest_month = df.loc[df["Sales"].idxmax(), "Date"]

print("\nHighest Monthly Sales:", highest_sales)
print("Highest Sales Month:", highest_month.strftime("%B %Y"))

# Lowest monthly sales
lowest_sales = df["Sales"].min()
lowest_month = df.loc[df["Sales"].idxmin(), "Date"]

print("\nLowest Monthly Sales:", lowest_sales)
print("Lowest Sales Month:", lowest_month.strftime("%B %Y"))

# Save cleaned dataset
df.to_csv("cleaned_sales_data.csv", index=False)

print("\nCleaned dataset saved successfully!")
