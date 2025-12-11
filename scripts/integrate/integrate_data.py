import os
import sqlite3
import pandas as pd

DB_PATH = os.path.join("data", "processed", "education_income.db")

EDU_TABLE = "education_clean"
INC_TABLE = "income_clean"
JOIN_TABLE = "education_income_join"


def income_tier(value):
    """
    Categorize income into tiers.
    Adjust thresholds as needed for analysis.
    """
    if value < 35000:
        return "Low income"
    elif value < 60000:
        return "Middle income"
    else:
        return "High income"


def main():
    print(f"Opening database: {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)

    # Load cleaned tables
    edu = pd.read_sql(f"SELECT * FROM {EDU_TABLE}", conn)
    inc = pd.read_sql(f"SELECT * FROM {INC_TABLE}", conn)

    print("Computing income tiers...")

    # Education dataset uses median income column (called 'median' after cleaning)
    edu["income_tier"] = edu["median"].apply(income_tier)

    # County income dataset uses per-capita income ('pci')
    inc["income_tier"] = inc["pci"].apply(income_tier)

    print("Integrating datasets based on income tier...")

    # Merge datasets by income tier
    integrated = edu.merge(inc, on="income_tier", suffixes=("_major", "_county"))

    print(f"Integrated dataset size: {len(integrated)} rows")
    print("Saving to SQLite...")

    # Save integrated table
    integrated.to_sql(JOIN_TABLE, conn, if_exists="replace", index=False)

    conn.close()
    print(f"Integration complete. Table '{JOIN_TABLE}' created.")


if __name__ == "__main__":
    main()
