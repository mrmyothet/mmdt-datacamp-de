import logging
import logging.config
import pandas as pd


def extract(file_name):

    # Read the sales data into a DataFrame
    sales_data = pd.read_parquet(f"../data/{file_name}", engine="fastparquet")
    return sales_data


def transform(raw_data):
    raw_data["order_date"] = pd.to_datetime(raw_data["order_date"], unit="ms")
    clean_data = raw_data.loc[raw_data["price_each"] < 10, :]

    # Create an info log regarding transformation
    logging.info("Transformed 'order_date' column to type 'datetime'.")

    # Create debug-level logs for the DataFrame before and after filtering
    logging.debug(f"Shape of the DataFrame before filtering: {raw_data.shape}")
    logging.debug(f"Shape of the DataFrame after filtering: {clean_data.shape}")

    return clean_data


raw_sales_data = extract("sales_data.parquet")
clean_sales_data = transform(raw_sales_data)
