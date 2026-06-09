import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Cleaned_Sales_Dataset.xlsx")

# ---------------- KPIs ----------------

total_sales = df["Total_Sales"].sum()
total_orders = df["Order_ID"].nunique()
average_order_value = df["Total_Sales"].mean()
total_customers = df["Customer_ID"].nunique()
total_quantity = df["Quantity"].sum()

print("========== KPI DASHBOARD ==========")
print("Total Sales :", total_sales)
print("Total Orders :", total_orders)
print("Average Order Value :", round(average_order_value,2))
print("Total Customers :", total_customers)
print("Total Quantity Sold :", total_quantity)

# Sales by Category

category_sales = df.groupby("Category")["Total_Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")
plt.title("Category Wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("dashboard_category_sales.png")
plt.show()

# Top Products

product_sales = df.groupby("Product")["Total_Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
product_sales.plot(kind="bar")
plt.title("Top 10 Products")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("top_products.png")
plt.show()

# City Sales

city_sales = df.groupby("City")["Total_Sales"].sum().sort_values(ascending=False)

plt.figure(figsize=(10,5))
city_sales.plot(kind="bar")
plt.title("City Wise Sales")
plt.xlabel("City")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("city_sales.png")
plt.show()

# Age Group Analysis

age_sales = df.groupby("Age_Group")["Total_Sales"].sum()

plt.figure(figsize=(7,5))
age_sales.plot(kind="pie",autopct="%1.1f%%")
plt.ylabel("")
plt.title("Sales by Age Group")
plt.savefig("age_group_sales.png")
plt.show()

print("\nDashboard Files Generated Successfully")