import pandas as pd

# pip install fastparquet

# Read the sales data into a DataFrame
sales_data = pd.read_parquet("../data/sales_data.parquet", engine="fastparquet")

# Check the data type of the columns of the DataFrames
print(sales_data.dtypes)

# Print the shape of the DataFrame, as well as the head
print(sales_data.shape)
print(sales_data.head())
