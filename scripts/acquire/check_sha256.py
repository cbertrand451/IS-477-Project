# scripts/acquire/check_sha256.py

import hashlib
import os

# return the SHA-256 checksum of a file
def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()

# Read the expected checksum from a .sha256 file
def read_expected(checksum_file):
    with open(checksum_file, "r") as f:
        line = f.readline().strip()
    # format: "<checksum>  <filename>"
    expected = line.split()[0]
    return expected

# compare actual vs expected checksum and print match/mismatch
def verify(data_path, checksum_path):
    actual = sha256(data_path)
    expected = read_expected(checksum_path)

    print(f"Checking: {data_path}")
    print(f"Expected: {expected}")
    print(f"Actual:   {actual}")

    if actual == expected:
        print("MATCH — file is correct.\n")
    else:
        print("MISMATCH — file was modified or corrupted.\n")


def main():
    verify(
        "data/raw/education/recent_grads.csv",
        "data/raw/education/recent_grads.sha256"
    )
    verify(
        "data/raw/income/counties_per_capita_income.csv",
        "data/raw/income/counties_per_capita_income.csv.sha256"
    )


if __name__ == "__main__":
    main()
