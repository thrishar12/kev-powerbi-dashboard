import pandas as pd

df = pd.read_csv("known_exploited_vulnerabilities.csv")

# 1. Convert date text into real dates
df["dateAdded"] = pd.to_datetime(df["dateAdded"])
df["dueDate"] = pd.to_datetime(df["dueDate"])

# 2. New columns
df["days_to_fix"] = (df["dueDate"] - df["dateAdded"]).dt.days
df["year_added"] = df["dateAdded"].dt.year
df["month_added"] = df["dateAdded"].dt.to_period("M").astype(str)

# 3. Ransomware flag: Known -> 1, otherwise 0
df["ransomware"] = (df["knownRansomwareCampaignUse"] == "Known").astype(int)

# 4. Fill missing CWE values
df["cwes"] = df["cwes"].fillna("Unknown")

# 5. Quick answers
print("Top 10 vendors:")
print(df["vendorProject"].value_counts().head(10))
print("\nEntries added per year:")
print(df.groupby("year_added").size())
print("\nRansomware share (%):", round(df["ransomware"].mean() * 100, 1))
print("\nDays to fix:")
print(df["days_to_fix"].describe())

# 6. Save a clean file for Power BI and Tableau
df.to_csv("kev_clean.csv", index=False)
print("\nSaved kev_clean.csv")