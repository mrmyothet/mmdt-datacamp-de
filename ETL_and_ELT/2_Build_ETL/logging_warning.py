import logging
import logging.config
import pandas as pd


def extract(file_name):

    # Read the sales data into a DataFrame
    sales_data = pd.read_parquet(f"../data/{file_name}", engine="fastparquet")
    return sales_data


def transform(raw_data):
    return raw_data.loc[raw_data["Total Price"] > 1000, :]


raw_sales_data = extract("sales_data.parquet")
try:
    # Attempt to transform DataFrame, log an info-level message
    clean_sales_data = transform(raw_sales_data)
    logging.info("Successfully filtered DataFrame by 'Total Price'")
    print(clean_sales_data.head())

except KeyError as ke:
    # Log a warning-level message
    logging.warning(f"{ke}: Cannot filter DataFrame by 'Total Price'")

    # Create the "Total Price" column, transform the updated DataFrame
    raw_sales_data["Total Price"] = (
        raw_sales_data["price_each"] * raw_sales_data["quantity_ordered"]
    )
    clean_sales_data = transform(raw_sales_data)
    print(clean_sales_data.head())
