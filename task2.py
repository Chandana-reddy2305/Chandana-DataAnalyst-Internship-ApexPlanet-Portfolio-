import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Cleaned_Sales_Dataset.xlsx")

print("First 5 Rows")
print(df.head())

print("\nSummary Statistics")
print(df.describe())

print("\nCategory Count")
print(df["Category"].value_counts())

print("\nGender Count")
print(df["Gender"].value_counts())

print("\nTotal Sales")
print(df["Total_Sales"].sum())

print("\nAverage Sales")
print(df["Total_Sales"].mean())

sales_by_category = df.groupby("Category")["Total_Sales"].sum()

plt.figure(figsize=(8,5))
sales_by_category.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("sales_by_category.png")
plt.show()

gender = df["Gender"].value_counts()

plt.figure(figsize=(6,6))
gender.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Gender Distribution")
plt.savefig("gender_distribution.png")
plt.show()

city_sales = df.groupby("City")["Total_Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
city_sales.plot(kind="bar")
plt.title("Top 10 Cities by Sales")
plt.xlabel("City")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("top10cities.png")
plt.show()

print("\nEDA Completed Successfully")