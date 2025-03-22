import pandas as pd
import os


def extract(file_name):

    # Read the sales data into a DataFrame
    sales_data = pd.read_parquet(f"../data/{file_name}", engine="fastparquet")
    return sales_data


def transform(raw_data):
    # Find the items prices less than 25 dollars
    return raw_data.loc[
        raw_data["price_each"] < 25, ["order_id", "product", "price_each", "order_date"]
    ]


def load(clean_data, file_path):
    # Write the data to a CSV file without the index column
    clean_data.to_csv(file_path, index=False)


raw_sales_data = extract("sales_data.parquet")
clean_sales_data = transform(raw_sales_data)

# Call the load function on the cleaned DataFrame
output_file_path = "transformed_sales_data.csv"
load(clean_sales_data, output_file_path)

assert os.path.exists(output_file_path)
