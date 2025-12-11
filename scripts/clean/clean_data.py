import os
import sqlite3
import pandas as pd

DB_PATH = os.path.join("data", "processed", "education_income.db")

# Table names
EDU_RAW = "education_raw"
EDU_CLEAN = "education_clean"

INC_RAW = "income_raw"
INC_CLEAN = "income_clean"


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Standardize column names: lowercase, underscores, strip spaces."""
    df = df.copy()
    df.columns = (
        df.columns
        .str.lower()
        .str.strip()
        .str.replace(" ", "_")
        .str.replace("-", "_")
    )
    return df


def clean_education(df: pd.DataFrame) -> pd.DataFrame:
    """Clean the FiveThirtyEight education dataset."""
    df = clean_column_names(df)

    # Drop rows with missing major or salary-related fields
    print("NA in 'major' before cleaning:", df['major'].isna().sum())
    print("NA in 'median' before cleaning:", df['median'].isna().sum())
    df = df.dropna(subset=["major", "median"])
    df = df.drop_duplicates()

    return df


def clean_income(df: pd.DataFrame) -> pd.DataFrame:
    """Clean the county income dataset."""

    df = clean_column_names(df)

    # Ensure expected columns exist
    expected_cols = [
        "county",
        "states",
        "pci",
        "household_income",
        "family_income",
        "population",
        "num_of_households"
    ]

    missing = [c for c in expected_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing expected columns: {missing}")

    # Rename 'states' -> 'state' for clarity
    df = df.rename(columns={"states": "state"})

    # Convert number related columns to numeric
    num_cols = ["pci", "household_income", "family_income", "population", "num_of_households"]
    for col in num_cols:
        df[col] = (df[col].astype(str).str.replace('$', '', regex=False).str.replace(',', '', regex=False).str.strip())
        df[col] = pd.to_numeric(df[col], errors="coerce")


    # Drop rows missing county, state, or per-capita income
    print("NA in 'county' before cleaning:", df['county'].isna().sum())
    print("NA in 'state' before cleaning:", df['state'].isna().sum())
    print("NA in 'pci' before cleaning:", df['pci'].isna().sum())
    df = df.dropna(subset=["county", "state", "pci"])

    # Clean county/state strings
    df["county"] = df["county"].str.strip().str.title()
    df["state"] = df["state"].str.strip().str.title()

    # Drop duplicates
    df = df.drop_duplicates()

    return df


def main():
    print(f"Opening database: {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)

    try:
        # Load raw tables
        df_edu = pd.read_sql(f"SELECT * FROM {EDU_RAW}", conn)
        df_inc = pd.read_sql(f"SELECT * FROM {INC_RAW}", conn)

        print("Cleaning education data...")
        df_edu_clean = clean_education(df_edu)

        print("Cleaning county income data...")
        df_inc_clean = clean_income(df_inc)

        # Write cleaned tables
        df_edu_clean.to_sql(EDU_CLEAN, conn, if_exists="replace", index=False)
        df_inc_clean.to_sql(INC_CLEAN, conn, if_exists="replace", index=False)

        print("\nClean tables created:")
        print(f" - {EDU_CLEAN}")
        print(f" - {INC_CLEAN}")

    finally:
        conn.close()
        print("Database connection closed.\n")


if __name__ == "__main__":
    main()
