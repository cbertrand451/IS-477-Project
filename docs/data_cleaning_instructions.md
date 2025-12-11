# Data Quality Assessment and Cleaning Documentation

This document describes the profiling and cleaning steps performed on the two datasets used in this project:  
- the FiveThirtyEight Recent Graduates dataset
- the Kaggle U.S. County Income dataset

---

## Data Profiling

### Education Dataset
- Inconsistent column naming conventions with mixed capitalization and spaces. (ex. "ShareWoman" vs. "Sample_size")
- Significant columns had no missing values

### County Income Dataset
- All expected columns were present.
- Numeric fields (pci, household_income) were stored as strings.
- Many numeric columns included commas and dollar signs
- No significant missing data detected.

---

## Data Cleaning Steps

### Education Dataset Cleaning
The following cleaning actions were applied:

- Standardized all column names (lowercase, underscores).
- Removed rows missing critical values (major, median).
- Removed duplicate records.
- Stored cleaned dataset as education_clean in SQLite.

### County Income Dataset Cleaning
Cleaning actions performed:

- Standardized column names (lowercase, removed spaces and dashes).
- Renamed the states field to state.
- Converted number fields (pci, household_income, family_income, population, num_of_households) to numeric types.
- Trimmed whitespace in county and state fields and standardized case.
- Removed rows missing critical fields (county, state, pci).
- Removed duplicates.
- Stored cleaned dataset as income_clean in SQLite.

---

