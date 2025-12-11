import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os

# Ensure results folder exists
os.makedirs("results", exist_ok=True)

DB_PATH = "data/processed/education_income.db"

def load_data():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql("SELECT * FROM education_income_join", conn)
    conn.close()
    return df

df = load_data()

# question 1
df_major = df[['major', 'median', 'income_tier']].drop_duplicates()
df_county = df[['county', 'state', 'pci', 'income_tier']].drop_duplicates()

# Summary statistics
major_summary = df_major['median'].describe()
county_summary = df_county['pci'].describe()

major_summary.to_csv("results/major_summary.csv")
county_summary.to_csv("results/county_summary.csv")

print("Major summary:\n", major_summary)
print("\nCounty summary:\n", county_summary)

plt.boxplot(
    [df_major['median'], df_county['pci']],
    labels=["Majors (Median Income)", "Counties (Per Capita Income)"]
)
plt.ylabel("Income ($)")
plt.title("Income Distribution: College Majors vs. U.S. Counties")
plt.savefig("results/boxplot_income_comparison.png")
plt.close()

# question 2
major_tier_counts = df_major['income_tier'].value_counts()

major_tier_counts.plot(kind='bar', title='Majors by Income Tier')
plt.ylabel("Number of Majors")
plt.savefig("results/majors_by_income_tier.png")
plt.close()

county_tier_counts = df_county['income_tier'].value_counts()

county_tier_counts.plot(kind='bar', title='Counties by Income Tier')
plt.ylabel("Number of Counties")
plt.savefig("results/counties_by_income_tier.png")
plt.close()


# question 3
major_std = df_major['median'].std()
county_std = df_county['pci'].std()

with open("results/variability.txt", "w") as f:
    f.write(f"Major income standard deviation: {major_std}\n")
    f.write(f"County PCI standard deviation: {county_std}\n")

print("Major income variability:", major_std)
print("County income variability:", county_std)

plt.hist(df_major['median'], bins=20, alpha=0.6, label='Majors')
plt.hist(df_county['pci'], bins=20, alpha=0.6, label='Counties')
plt.xlabel("Income ($)")
plt.ylabel("Frequency")
plt.legend()
plt.title("Income Variability Across Majors and Counties")
plt.savefig("results/income_histogram_variability.png")
plt.close()
