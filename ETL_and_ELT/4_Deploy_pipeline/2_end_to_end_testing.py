import pandas as pd
from pipeline_utils import extract, transform, load

raw_file_path = (
    "/home/myothet/myothet/mmdt-datacamp-de/ETL_and_ELT/data/raw_tax_data.csv"
)
clean_file_path = "../data/clean_tax_data.parquet"

# Trigger the data pipeline to run three times
for attempt in range(0, 3):
    print(f"Attempt: {attempt}")
    raw_tax_data = extract(raw_file_path)
    clean_tax_data = transform(raw_tax_data)
    load(clean_tax_data, clean_file_path)

    # Print the shape of the cleaned_tax_data DataFrame
    print(f"Shape of clean_tax_data: {clean_tax_data.shape}")

# Read in the loaded data, check the shape
to_validate = pd.read_parquet(clean_file_path)
print(f"Final shape of cleaned data: {to_validate.shape}")
