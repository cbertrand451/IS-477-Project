import subprocess
import os

def run(script_path):
    print(f"\nRunning: {script_path}")
    result = subprocess.run(["python", script_path], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)
        raise RuntimeError(f"Script failed: {script_path}")
    print(f"Completed: {script_path}")


def main():
    print("Starting full workflow automation...\n")
    # acquire data
    run("scripts/acquire/fetch_education.py")
    #manual dataset only needs checksum creation
    run("scripts/acquire/income_sha256.py")
    # check the integrity of the data using checksum and sha
    run("scripts/acquire/check_sha256.py")
    # load into database
    run("scripts/load/load_to_sqlite.py")
    # clean data
    run("scripts/clean/clean_data.py")
    # integrate datasets
    run("scripts/integrate/integrate_data.py")
    # analyze 
    run("scripts/analyze/analyze_data.py")

    print("\nWorkflow finsihed\n")

if __name__ == "__main__":
    main()
