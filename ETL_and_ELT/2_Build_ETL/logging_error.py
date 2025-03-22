import logging
import pandas as pd


def extract(file_path):
    return pd.read_parquet(file_path)


# Update the pipeline to include a try block
try:
    # Attempt to read in the file
    raw_sales_data = extract("sales_data.parquet")

# Catch the FileNotFoundError
except FileNotFoundError as file_not_found:
    # Write an error-level log
    logging.error(file_not_found)
