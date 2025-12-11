# scripts/load/load_to_sqlite.py

import os
import sqlite3
import pandas as pd

# Paths to raw CSV files
EDUCATION_CSV = os.path.join("data", "raw", "education", "recent_grads.csv")
INCOME_CSV = os.path.join("data", "raw", "income", "counties_per_capita_income.csv")

# Path to SQLite database
DB_DIR = os.path.join("data", "processed")
DB_PATH = os.path.join(DB_DIR, "education_income.db")

# Table names
EDUCATION_TABLE = "education_raw"
INCOME_TABLE = "income_raw"


def ensure_dir(path: str) -> None:
    """Ensure that a directory exists."""
    os.makedirs(path, exist_ok=True)


def load_csv_to_sqlite(csv_path: str, conn: sqlite3.Connection, table_name: str) -> None:
    """
    Load a CSV file into a SQLite table.
    If the table already exists, it will be replaced.
    """
    print(f"Loading {csv_path} into table '{table_name}'...")
    df = pd.read_csv(csv_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    print(f"Loaded {len(df)} rows into '{table_name}'.\n")


def main() -> None:
    # Make sure the processed directory exists
    ensure_dir(DB_DIR)

    print(f"Creating / updating SQLite database at: {DB_PATH}")
    conn = sqlite3.connect(DB_PATH)

    try:
        load_csv_to_sqlite(EDUCATION_CSV, conn, EDUCATION_TABLE)
        load_csv_to_sqlite(INCOME_CSV, conn, INCOME_TABLE)
        print("All tables loaded successfully.")
    finally:
        conn.close()
        print("Database connection closed.")


if __name__ == "__main__":
    main()
