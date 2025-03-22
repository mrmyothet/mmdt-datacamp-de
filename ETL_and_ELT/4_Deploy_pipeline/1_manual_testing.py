import pandas as pd
from extract_transform_load import extract, transform, load

file_path = "/home/myothet/myothet/mmdt-datacamp-de/ETL_and_ELT/data/raw_tax_data.csv"

# Extract and transform tax_data
raw_tax_data = extract(file_path)
clean_tax_data = transform(raw_tax_data)
load(clean_tax_data, "../data/clean_tax_data.parquet")

# Check the shape of the raw_tax_data DataFrame, compare to the clean_tax_data DataFrame
print(f"Shape of raw_tax_data: {raw_tax_data.shape}")
print(f"Shape of clean_tax_data: {clean_tax_data.shape}")


# Read in the loaded data, observe the head of each
to_validate = pd.read_parquet("../data/clean_tax_data.parquet")

print(clean_tax_data.head(3))
print(to_validate.head(3))


# Check that the DataFrames are equal
print(to_validate.equals(clean_tax_data))
