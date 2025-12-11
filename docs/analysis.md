# Analysis

This section presents the results of the comparison between incomes of recent U.S. college graduates and incomes across U.S. counties. 

The purpose of the analysis is to compare income patterns across two distinct populations:
1. Recent U.S. college graduates (by major), and  
2. U.S. counties (by per capita income).

The analysis addresses the three research questions below.

---

## RQ1: How do income levels for recent college graduates compare to income levels across U.S. counties?

The boxplot comparison shows that graduates in many majors earn median incomes that differ substantially from county-level per-capita income. STEM majors typically occupy the upper end of the distribution, whereas county PCI is generally lower and spread more widely. This reflects differences in labor-market outcomes across fields of study compared to structural economic conditions by geography.

---

## RQ2: How are graduates and counties distributed across income tiers?

Majors and counties show different patterns when grouped into low, middle, and high-income tiers. While majority of majors are still clustered in the low-income group, there is a noticeable group in the high-income, and even bigger group in middle-income. Counties continue to have a pronounced presence in the low-income tier. This suggests that established career paths often result in higher income brackets compared to the environments in which people live.

---

## RQ3: Do income tiers exhibit similar variability among majors and among counties?

The standard deviation of major-level income is significantly larger than that of county PCI. This indicates that graduates experience wider income inequality, while counties within the same income_tier tend to have more similar income levels. Countiesmay show less variability, but they also represent a much larger population than the majors are able to. 

# Analysis Steps

### Loading the Integrated Dataset

The first step in the analysis pipeline is loading the integrated dataset produced by the income-tier join.

Then, two seperate tables were created to see different perspectoves betweeen majors and counties.

- df_major (one row per major)

- df_county (one row per county)

### Summary Statistics 

To compare overall income levels between majors and counties, descriptive statistics are computed for each dataset.

These summaries include:

- mean
- standard deviation
- min/max income
- quartiles

These statistics support Research Question 1 by providing a numeric comparison of income distributions.

### Distribution Comparison 

A boxplot is used to visually compare the distribution of median incomes (majors) against per capita income (counties).

This visualization shows:

- differences in median values
- differences in variability
- presence of high-income majors relative to high-income counties

This served as a helpful visualization for Research Question 1. 

### Income Tier Distribution 

To answer Research Question 2, the number of majors and counties in each income tier is computed. A barchart served as the most efficient way to visualize these counts between the two topics. 

These visualizations support comparisons across income categories and help identify concentration patterns (e.g., many majors in the middle tier vs. many counties in the low tier).

### Variability Analysis 

To answer Research Question 3, income variability is quantified using standard deviation.

This comparison highlights differences in income inequality across majors and counties.

To supplement the numeric comparison, a histogram is used to visualize variability.

---

# Interpretation


Based on the results above:

- Majors typically show higher median incomes than county PCI values.
- Majors cluster more heavily into middle and high income tiers.
- Counties show a wider range of incomes at the lower end, reflecting broader economic conditions.
- Income variability among majors is larger, driven by high-paying fields such as engineering and computer science.
- County incomes show less variability overall but represent larger populations.

---

# Output Files

All analysis outputs are saved in the results directory:

- major_summary.csv
- county_summary.csv
- variability.txt
- boxplot_income_comparison.png
- majors_by_income_tier.png
- counties_by_income_tier.png
- income_histogram_variability.png