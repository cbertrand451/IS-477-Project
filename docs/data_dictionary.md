# Data Dictionary 

This data dictionary describes all variables used in the project across the raw datasets, cleaned datasets, and integrated dataset.  

---

# Education Dataset (Recent Graduates)

**Source:** FiveThirtyEight (recent graduates dataset)  
**File:** data/raw/education/recent_grads.csv
**Cleaned Table:** education_clean in education_income.db

### Variables

| Variable | Type | Description |
|---------|------|-------------|
| Rank | int | Rank of major by median earnings. |
| Major_code | int | Major code (FO1DP) used by the ACS PUMS dataset. |
| Major | string | Description of the college major. |
| Major_category | string | Category of the major (e.g., Engineering, Business). |
| Total | int | Total number of people with this major. |
| Sample_size | int | Unweighted ACS sample size for full-time, year-round workers (used for earnings). |
| Men | int | Number of male graduates. |
| Women | int | Number of female graduates. |
| ShareWomen | float | Proportion of graduates who are women (Women / Total). |
| Employed | int | Number employed (ACS ESR == 1 or 2). |
| Full_time | int | Number employed full-time (35+ hours per week). |
| Part_time | int | Number employed part-time (< 35 hours per week). |
| Full_time_year_round | int | Full-time and year-round workers (≥50 weeks & ≥35 hours/week). |
| Unemployed | int | Number unemployed (ACS ESR == 3). |
| Unemployment_rate | float | Unemployed divided by labor force (Unemployed / (Employed + Unemployed)). |
| Median | int | Median earnings of full-time, year-round workers. |
| P25th | int | 25th percentile of earnings. |
| P75th | int | 75th percentile of earnings. |
| College_jobs | int | Number of graduates employed in jobs requiring a college degree. |
| Non_college_jobs | int | Number of graduates employed in jobs *not* requiring a college degree. |
| Low_wage_jobs | int | Number employed in low-wage service occupations. |
| income_tier *(derived)* | string (Low, Middle, High) | Income category based on Median value. |

---


# County Income Dataset (Manually Downloaded)

**Source:** Kaggle – U.S. Counties by Per Capita Income  
**File:** data/raw/income/counties_per_capita_income.csv  
**Cleaned Table:** income_clean in education_income.db

### Variables

| Variable | Type | Description |
|---------|------|-------------|
| county | string | Name of the U.S. county. |
| states | string | State in which the county is located. |
| pci | int | Per capita income for the county. |
| household_income | int | Median household income for the county. |
| family_income | int | Median family income for the county. |
| population | int | Population of the county. |
| num_of_households | int | Number of households in the county. |
| income_tier *(derived)* | string (Low, Middle, High) | Income category derived from pci. |

---

# Integrated Dataset

**Table:** education_income_join in education_income.db` 
**Description:**  
A many-to-many join between education_clean and income_clean based on the shared derived variable income_tier.

### Variables from Education Dataset

| Variable | Type | Description |
|---------|------|-------------|
| major | string | Name of college major. |
| median | int | Median income for the major. |
| income_tier | string | Income category assigned by major median income. |

### Variables from County Dataset

| Variable | Type | Description |
|---------|------|-------------|
| county | string | County name. |
| state | string | U.S. state. |
| pci | int | Per capita income for the county. |
| income_tier | string | Income category assigned by county PCI (same grouping). |

### Notes on Integration
- Integration is performed on the shared variable income_tier.
- Because income tier categories map many majors to many counties, the resulting table has a **many-to-many** structure.
- This dataset supports comparative analysis of economic outcomes across education and geography.

---

# Derived Variables

### income_tier (Education Dataset)
Derived from the median income of each major:

| Tier | Definition |
|------|------------|
| **Low** | < $35,000 |
| **Middle** | $35,000 – $59,999 |
| **High** | ≥ $60,000 |

### income_tier (County Dataset)
Same definition as above, using per capita income (pci).

---

# Citation Information

- **Education Data Source:** FiveThirtyEight - “Recent College Graduates Dataset.”  
- **Income Data Source:** Kaggle - U.S. Counties by Per Capita Income” (Public Domain License).  

