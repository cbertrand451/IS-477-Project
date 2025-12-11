# Data Acquisition Instructions

This document describes the process used to acquire the two static datasets used in this project.  

---

# Overview of Data Sources

## Dataset 1: College Major Outcomes (FiveThirtyEight)
- **URL:** https://raw.githubusercontent.com/fivethirtyeight/data/master/college-majors/recent-grads.csv  
- **Format:** CSV  
- **Source:** FiveThirtyEight public data repository  
- **Contents:** Employment, salary, unemployment rates, and demographic statistics for U.S. college majors.

## Dataset 2: U.S. County Income Dataset
- **Source:** Kaggle: *United States Counties by Per Capita Income*  
- **License:** Public Domain (no restrictions on use)  
- **URL:** https://www.kaggle.com/datasets/kabhishm/united-states-counties-by-per-capita-income  
- **Access Method:** Manual download due to Kaggle download restrictions  
- **Format:** CSV  
- **Stored at:** `data/raw/income/counties_per_capita_income.csv`

This dataset includes county-level income metrics, including income per capita and median household incomes.

Since Kaggle does not provide a direct programmatic download URL without authentication, the dataset was manually downloaded and saved in the project directory. The version used in this project is static and does not change over time.

---

# Files Created by Acquisition Scripts and Manual Downloads

Running the acquisition scripts produces the following files:

- data/raw/education/recent_grads.csv
- data/raw/education/recent_grads.sha256

Manually added the following file:
- data/raw/income/counties_per_capita_income.csv

Generated checksum file for the manually added file:
- data/raw/income/counties_per_capita_income.csv.sha256

Raw data files are stored in `data/raw/` and never modified.  

---

# Reproducing Data Acquisition

To reproduce the acquisition process, run the following scripts from the project root:

### Step 1: Download College Major Outcomes

python scripts/acquire/fetch_education.py

### Step 2: Download U.S. County Income Dataset

Manually download the dataset from Kaggle at the provided URL and save it to:

data/raw/income/counties_per_capita_income.csv

URL: https://www.kaggle.com/datasets/kabhishm/united-states-counties-by-per-capita-income

Then run the following script to generate the checksum file for the manually downloaded dataset:
python scripts/acquire/income_sha256.py

The scripts will download datasets and create the necessary checksum files for integrity verification.
---

# Verify Data Integrity

Verify the integrity of the downloaded files by runnning the check sha256 python script:

python scripts/acquire/check_sha256.py

This will compare the computed SHA-256 checksums against the stored checksum files to ensure data integrity. an output of "MATCH" means a succesful verification, and "MISMATCH" means unsuccessful.

---

# Licensing and Ethical Considerations

### FiveThirtyEight Data License

The dataset is provided for public reuse for educational and analytical purposes. Attribution is recommended.

### Kaggle county income dataset:

This dataset is licensed as Public Domain. It contains no personally identifiable information and is safe for redistribution and educational use.

No privacy, security, or consent concerns apply to either dataset.