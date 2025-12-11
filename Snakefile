# directories
RAW_DIR = "data/raw"
PROC_DIR = "data/processed"
RESULTS_DIR = "results"

# database path
DB = f"{PROC_DIR}/education_income.db"

# create rule for default targets
rule all:
    input:
        DB,
        f"{RESULTS_DIR}/major_summary.csv",
        f"{RESULTS_DIR}/county_summary.csv",
        f"{RESULTS_DIR}/boxplot_income_comparison.png",
        f"{RESULTS_DIR}/majors_by_income_tier.png",
        f"{RESULTS_DIR}/counties_by_income_tier.png",
        f"{RESULTS_DIR}/income_histogram_variability.png",
        f"{RESULTS_DIR}/variability.txt"

# get education dataset
rule fetch_education:
    output:
        f"{RAW_DIR}/education/recent_grads.csv"
    shell:
        "python scripts/acquire/fetch_education.py"

# generate sha256 for county income dataste
rule sha256_income:
    input:
        f"{RAW_DIR}/income/counties_per_capita_income.csv"
    output:
        f"{RAW_DIR}/income/counties_per_capita_income.csv.sha256"
    shell:
        "python scripts/acquire/income_sha256.py"

# check dta integrity with sha256
rule verify_sha256:
    input:
        edu_csv = "data/raw/education/recent_grads.csv",
        edu_sha = "data/raw/education/recent_grads.sha256",
        inc_csv = "data/raw/income/counties_per_capita_income.csv",
        inc_sha = "data/raw/income/counties_per_capita_income.csv.sha256"
    output:
        "data/raw/.verified"   
    shell:
        "python scripts/acquire/check_sha256.py && touch {output}"

# load data into sqlite
rule load_to_db:
    input:
        edu=f"{RAW_DIR}/education/recent_grads.csv",
        inc=f"{RAW_DIR}/income/income_by_county.csv",
        verified = "data/raw/.verified"
    output:
        "data/processed/.db_loaded"
    shell:
        "python scripts/load/load_to_db.py"

# clean data
rule clean_data:
    input:
        "data/processed/.db_loaded"
    output:
        "data/processed/.db_cleaned"
    shell:
        "python scripts/clean/clean_data.py"

# integrate
rule integrate:
    input:
        "data/processed/.db_cleaned"
    output:
        "data/processed/.db_integrated"
    shell:
        "python scripts/integrate/integrate_data.py"

# analysis
rule analyze:
    input:
        "data/processed/.db_integrated"
    output:
        expand("results/{file}", file=[
            "major_summary.csv",
            "county_summary.csv",
            "boxplot_income_comparison.png",
            "majors_by_income_tier.png",
            "counties_by_income_tier.png",
            "income_histogram_variability.png",
            "variability.txt"
        ])
    shell:
        "python scripts/analyze/analyze_data.py"
