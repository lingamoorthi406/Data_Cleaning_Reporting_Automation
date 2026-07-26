import pandas as pd

# Load dataset
df = pd.read_csv("data/sales data.csv")

print("Original Shape:", df.shape)

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values
df = df.fillna("Unknown")

# Save cleaned data
df.to_csv("output/cleaned_data.csv", index=False)

print("Cleaned Shape:", df.shape)
print("Cleaning Completed Successfully!")
print("\n========== DATASET INFORMATION ==========")
print(df.info())

print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== DUPLICATES ==========")
print("Duplicate Rows:", df.duplicated().sum())
import matplotlib.pyplot as plt

# Sales by Category
sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))
sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()

plt.savefig("charts/sales_by_category.png")
plt.close()
profit = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8,5))
profit.plot(kind="pie", autopct="%1.1f%%")
plt.title("Profit Distribution")
plt.ylabel("")
plt.savefig("charts/profit_distribution.png")
plt.close()
with open("output/report.txt", "w") as f:
    f.write("DATA CLEANING REPORT\n")
    f.write("====================\n")
    f.write(f"Rows: {df.shape[0]}\n")
    f.write(f"Columns: {df.shape[1]}\n")
    f.write(f"Duplicates: {df.duplicated().sum()}\n")

print("Report Created Successfully!")