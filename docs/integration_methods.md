# Integration Documentation

This document describes the conceptual model, integration schema, and workflow steps used to integrate the two cleaned datasets used in the project:  
- the FiveThirtyEight Recent Graduates dataset (education_clean) and  
- the Kaggle U.S. County Income dataset (income_clean).

The purpose of this integration is to create a unified dataset that supports comparative analysis of income patterns across majors and counties.

---

# Conceptual Integration Model

Because the datasets describe different units of analysis, majors vs. counties, and do not share a common geographic or demographic key, a direct relational join is not possible.

Instead, integration is achieved through the creation of a shared new variable, which categorizes each entity into one of three levels:

- **Low income** (< \$35,000)
- **Middle income** (\$35,000–\$60,000)
- **High income** (≥ \$60,000)

I named this variable 'income tier'.

The conceptual model is:

1. educacation clean (major incomes) --> derive income_tier from median income

2. income_clean (counties incomes) --> derive income_tier from per capita income

3. join education_clean and income_clean on income_tier

4. new integrated dataset

This new table represents a many-to-many relationship between majors and counties, because multiple counties and majors can share the same tier. 

---

# Integration Schema

Below is the schema of the tables involved.

## education_clean (input)

- major: name of college major
- median: median income for recent graduates

Derived field:
- income_tier (Low/Middle/High)

## income_clean (input)

- county: county name
- state: U.S. state
- pci: per capita income                           

Derived field:
- income_tier (Low/Middle/High)

---

# Integration Steps

Below are the exact steps used to integrate the two datasets:

### Load Cleaned Tables

Both education_clean and income_clean were read from the SQLite database created during the cleaning phase. 

edu = pd.read_sql("SELECT * FROM education_clean", conn)
inc = pd.read_sql("SELECT * FROM income_clean", conn)

### Create income tier variables

For education (by median income):

edu["income_tier"] = edu["median"].apply(income_tier)


For counties (by per capita income):

inc["income_tier"] = inc["pci"].apply(income_tier)


This creates a shared, interpretable categorical variable enabling integration.

### Perform Integration

A join is performed on the derived income_tier key. 

integrated = edu.merge(inc, on="income_tier")

### Store Integrated Dataset

The output table is written to the processed SQLite database. 

integrated.to_sql("education_income_join", conn, if_exists="replace", index=False)