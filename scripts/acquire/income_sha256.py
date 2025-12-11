# scripts/acquire/make_sha256.py

import hashlib
import os

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

def write_sha256_file(data_path):
    # Get filename only (e.g., income_by_county.csv)
    filename = os.path.basename(data_path)

    # Compute hash
    checksum = sha256(data_path)

    # Build .sha256 path
    sha_path = data_path + ".sha256"

    # Write hash + filename in required format
    with open(sha_path, "w") as f:
        f.write(f"{checksum}  {filename}\n")

    print(f"SHA-256 file created: {sha_path}")
    print(f"Checksum: {checksum}")

def main():
    # CHANGE THIS to the dataset you manually downloaded
    data_path = "data/raw/income/counties_per_capita_income.csv"

    if not os.path.exists(data_path):
        print("File not found:", data_path)
        return

    write_sha256_file(data_path)

if __name__ == "__main__":
    main()
