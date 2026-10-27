
import pandas as pd
import numpy as np

# Load cleaned dataset
df = pd.read_csv("cleaned_customer_churn.csv")

# Overall customer churn
total_customers = df["customerID"].nunique()
churned = (df["Churn"] == "Yes").sum()
churn_rate = np.mean(df["Churn"] == "Yes") * 100

print("CUSTOMER CHURN ANALYSIS")
print("-" * 35)
print("Total Customers:", total_customers)
print("Churned Customers:", churned)
print(f"Overall Churn Rate: {churn_rate:.2f}%")

# Churn by contract type
print("\nCHURN BY CONTRACT TYPE")
contract_churn = df.groupby("Contract")["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
)
print(contract_churn.round(2))

# Churn by internet service
print("\nCHURN BY INTERNET SERVICE")
internet_churn = df.groupby("InternetService")["Churn"].apply(
    lambda x: (x == "Yes").mean() * 100
)
print(internet_churn.round(2))

# Average monthly charges
print("\nAVERAGE MONTHLY CHARGES")
charges = df.groupby("Churn")["MonthlyCharges"].mean()
print(charges.round(2))

# Average customer tenure
print("\nAVERAGE TENURE IN MONTHS")
tenure = df.groupby("Churn")["tenure"].mean()
print(tenure.round(2))

# Save analysis results
contract_churn.to_csv("churn_by_contract.csv")
internet_churn.to_csv("churn_by_internet_service.csv")

print("\nAnalysis complete!")
print("Analysis result files saved successfully!")
