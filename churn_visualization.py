
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("cleaned_customer_churn.csv")

# Convert TotalCharges to numeric
df["TotalCharges"] = pd.to_numeric(
    df["TotalCharges"], errors="coerce"
)

# Chart 1: Customers who stayed vs churned
churn_counts = df["Churn"].value_counts()

plt.figure(figsize=(7, 5))
churn_counts.plot(kind="bar")
plt.title("Customer Churn Analysis")
plt.xlabel("Customer Status")
plt.ylabel("Number of Customers")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("customer_churn_chart.png")
plt.show()

# Chart 2: Churn by contract type
contract_churn = pd.crosstab(
    df["Contract"], df["Churn"]
)

contract_churn.plot(kind="bar", figsize=(8, 5))
plt.title("Customer Churn by Contract Type")
plt.xlabel("Contract Type")
plt.ylabel("Number of Customers")
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig("churn_by_contract_chart.png")
plt.show()

# Chart 3: Monthly charges by churn status
charges = df.groupby("Churn")[
    "MonthlyCharges"
].mean()

plt.figure(figsize=(7, 5))
charges.plot(kind="bar")
plt.title("Average Monthly Charges by Churn Status")
plt.xlabel("Customer Status")
plt.ylabel("Average Monthly Charges")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("monthly_charges_by_churn.png")
plt.show()

print("All charts created and saved successfully!")
