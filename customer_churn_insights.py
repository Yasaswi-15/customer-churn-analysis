
import pandas as pd
import numpy as np

# Load cleaned dataset
df = pd.read_csv("cleaned_customer_churn.csv")

# Convert columns to numeric
df["tenure"] = pd.to_numeric(df["tenure"], errors="coerce")
df["MonthlyCharges"] = pd.to_numeric(
    df["MonthlyCharges"], errors="coerce"
)

# Overall customer analysis
total_customers = len(df)
churned_customers = (df["Churn"] == "Yes").sum()
churn_rate = (churned_customers / total_customers) * 100

print("CUSTOMER CHURN ANALYSIS")
print("-----------------------")
print("Total Customers:", total_customers)
print("Customers Who Left:", churned_customers)
print("Customers Who Stayed:", (df["Churn"] == "No").sum())
print("Churn Rate:", round(churn_rate, 2), "%")

# Churn analysis by category
for column in ["Contract", "InternetService"]:
    print("\nChurn Analysis by", column)
    print("-----------------------")

    result = df.groupby(column, dropna=False).agg(
        Total_Customers=("Churn", "size"),
        Churned_Customers=(
            "Churn", lambda x: (x == "Yes").sum()
        )
    )

    result["Churn_Rate_Percent"] = (
        result["Churned_Customers"]
        / result["Total_Customers"] * 100
    ).round(2)

    print(result)

# Compare average tenure and monthly charges
print("\nAverage Customer Details")
print("------------------------")

print(df.groupby("Churn")[["tenure", "MonthlyCharges"]].mean().round(2))


# NumPy: Group customers based on tenure
df["TenureGroup"] = np.where(
    df["tenure"] < 12,
    "Less than 1 year",
    np.where(
        df["tenure"] < 24,
        "1 to 2 years",
        "2 years or more"
    )
)

# Analyze churn by tenure group
tenure_analysis = df.groupby("TenureGroup").agg(
    Total_Customers=("Churn", "size"),
    Churned_Customers=(
        "Churn", lambda x: (x == "Yes").sum()
    )
)

tenure_analysis["Churn_Rate_Percent"] = (
    tenure_analysis["Churned_Customers"]
    / tenure_analysis["Total_Customers"] * 100
).round(2)

print("\nChurn Analysis by Customer Tenure")
print(tenure_analysis)

tenure_analysis.to_csv("final_tenure_analysis.csv")

# Save analysis results
df.groupby("Contract").agg(
    Total_Customers=("Churn", "size"),
    Churned_Customers=(
        "Churn", lambda x: (x == "Yes").sum()
    )
).to_csv("final_contract_analysis.csv")

df.groupby("InternetService").agg(
    Total_Customers=("Churn", "size"),
    Churned_Customers=(
        "Churn", lambda x: (x == "Yes").sum()
    )
).to_csv("final_internet_analysis.csv")

print("\nFinal analysis completed successfully!")
print("Analysis files saved successfully!")
