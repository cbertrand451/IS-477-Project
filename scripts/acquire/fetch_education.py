# scripts/acquire/fetch_education.py

import os
import hashlib
import requests

URL = "https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/recent-grads.csv"

OUTPUT_DIR = os.path.join("data", "raw", "education")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "recent_grads.csv")
CHECKSUM_PATH = os.path.join(OUTPUT_DIR, "recent_grads.sha256")


def ensure_dir(path):
    os.makedirs(path, exist_ok=True)


def download_file(url, output_path):
    print(f"Downloading: {url}")
    r = requests.get(url)
    r.raise_for_status()

    ensure_dir(os.path.dirname(output_path))

    with open(output_path, "wb") as f:
        f.write(r.content)

    print("Saved to:", output_path)


def compute_sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def write_checksum(data_path, checksum_path):
    checksum = compute_sha256(data_path)
    with open(checksum_path, "w") as f:
        f.write(f"{checksum}  {os.path.basename(data_path)}\n")

    print("Checksum saved to:", checksum_path)
    print("SHA-256:", checksum)


def main():
    download_file(URL, OUTPUT_PATH)
    write_checksum(OUTPUT_PATH, CHECKSUM_PATH)


if __name__ == "__main__":
    main()
