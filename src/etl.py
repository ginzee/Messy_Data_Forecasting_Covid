import argparse
import os
import pandas as pd
from lib.load_data import load_data
from lib.clean_data import clean_data
from lib.merge_data import merge_data_country, group_data, complete_merge
from lib.filter_data import filter_data, filter_datasets_by_date

def parse_args():
    parser = argparse.ArgumentParser(description="ETL Process for Covid-19 data.")
    parser.add_argument("path", type=str, help="Folder containing the ZIP files.")
    parser.add_argument("-o", "--output", type=str, help="Output folder for final_merge.csv. Default: current directory.")
    parser.add_argument("-start", "--start_date", type=str, default="2020-01-02", help="Start date (YYYY-MM-DD). Default: 2020-01-02")
    parser.add_argument("-end", "--end_date", type=str, default="2022-08-22", help="End date (YYYY-MM-DD). Default: 2022-08-22")
    parser.add_argument("-countries", "--countries", type=str, help="Comma-separated list of countries to filter. Default: all")
    return parser.parse_args()

def run_etl(input_path, output_path, start_date, end_date, countries):
    # 1. Load data
    demographics, epidemiology, vaccinations, hospitalizations, health, index = load_data(input_path)

    # 2. Clean data
    demographics, epidemiology, vaccinations, hospitalizations, health, index = clean_data(
        demographics, epidemiology, vaccinations, hospitalizations, health, index
    )

    # 3. Filter by date BEFORE merges
    # This step will filter epidemiology, vaccinations, and hospitalizations by the given date range
    demographics, epidemiology, vaccinations, hospitalizations, health, index = filter_datasets_by_date(
        demographics, epidemiology, vaccinations, hospitalizations, health, index, start_date, end_date
    )

    # 4. Merge country data
    demographics, epidemiology, vaccinations, hospitalizations, health = merge_data_country(
        demographics, epidemiology, vaccinations, hospitalizations, health, index
    )

    # 5. Group and aggregate data
    demographics, epidemiology, vaccinations, hospitalizations, health = group_data(
        demographics, epidemiology, vaccinations, hospitalizations, health
    )

    # 6. Complete merge of all datasets
    complete_merge_data = complete_merge(demographics, epidemiology, vaccinations, hospitalizations, health)

    # 7. Filter by countries if requested (date filter already applied earlier)
    complete_merge_data = filter_data(complete_merge_data, start_date, end_date, countries)

    # 8. Save final result
    output_file = os.path.join(output_path, "final_merge.csv") if output_path else "final_merge.csv"
    complete_merge_data.to_csv(output_file, index=False)
    print(f"final_merge.csv saved at {output_file}")

if __name__ == "__main__":
    args = parse_args()
    input_path = args.path
    output_path = args.output if args.output else ""
    start_date = args.start_date
    end_date = args.end_date
    countries = args.countries

    run_etl(input_path, output_path, start_date, end_date, countries)

