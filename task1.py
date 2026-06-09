import pandas as pd

# Load the dataset
df = pd.read_excel("ApexPlanet_DataAnalytics_Dataset.xlsx")

# Display first 5 rows
print("========== FIRST 5 ROWS ==========")
print(df.head())

# Display dataset information
print("\n========== DATASET INFO ==========")
print(df.info())

# Display missing values
print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

# Display duplicate rows
print("\n========== DUPLICATE ROWS ==========")
print(df.duplicated().sum())

# Fill missing Age values with median
if "Age" in df.columns:
    df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing City values with mode
if "City" in df.columns:
    df["City"] = df["City"].fillna(df["City"].mode()[0])

# Remove duplicate rows
df = df.drop_duplicates()

# Convert Order_Date to datetime
if "Order_Date" in df.columns:
    df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Standardize text columns
text_columns = ["Gender", "City", "Product", "Category", "Customer_Name"]

for col in text_columns:
    if col in df.columns:
        df[col] = df[col].astype(str).str.title().str.strip()

# Create Age_Group feature
if "Age" in df.columns:
    df["Age_Group"] = pd.cut(
        df["Age"],
        bins=[0, 18, 35, 50, 100],
        labels=["Teen", "Young Adult", "Adult", "Senior"]
    )

# Save cleaned dataset
df.to_excel("Cleaned_Sales_Dataset.xlsx", index=False)

print("\n===================================")
print("DATA CLEANING COMPLETED SUCCESSFULLY")
print("Output file created:")
print("Cleaned_Sales_Dataset.xlsx")
print("===================================")