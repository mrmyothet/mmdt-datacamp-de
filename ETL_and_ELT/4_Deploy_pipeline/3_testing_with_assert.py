import pandas as pd
from extract_transform_load import extract, transform


raw_file_path = "../data/raw_tax_data.csv"
clean_file_path = "../data/clean_tax_data.parquet"

raw_tax_data = extract(raw_file_path)
clean_tax_data = transform(raw_tax_data)

# Validate the number of columns in the DataFrame
assert len(clean_tax_data.columns) == 5


# Assert that clean_tax_data is an instance of a pd.DataFrame
assert isinstance(clean_tax_data, pd.DataFrame)
# assert isinstance(clean_tax_data, str)

# Assert that clean_tax_data takes is an instance of a string
try:
    assert isinstance(clean_tax_data, str)
except Exception as e:
    print(f"{type(clean_tax_data)} is not a string: ", e)
