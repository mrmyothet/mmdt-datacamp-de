import pandas as pd


def extract(file_name):

    # Read the sales data into a DataFrame
    sales_data = pd.read_parquet(f"../data/{file_name}", engine="fastparquet")
    return sales_data


def transform(raw_data):

    # Convert the "Order Date" column to type datetime

    """
    raw_data["order_date"] = pd.to_datetime(
        raw_data["order_date"], format="%Y%m%d%H%M%S"
    )
    """

    raw_data["order_date"] = pd.to_datetime(raw_data["order_date"], unit="ms")

    # Only keep items under ten dollars
    raw_data = raw_data.loc[raw_data["price_each"] < 10, :]

    # Only keep rows with `Quantity Ordered` greater than 1
    clean_data = raw_data.loc[raw_data["quantity_ordered"] > 1, :]

    # Only keep columns "Order Date", "Quantity Ordered", and "Purchase Address"
    clean_data = clean_data.loc[
        :, ["order_date", "quantity_ordered", "purchase_address"]
    ]

    # Return the filtered DataFrame
    return clean_data


# Extract data from the sales_data.parquet path
raw_sales_data = extract("sales_data.parquet")
print(raw_sales_data.head())

clean_data = transform(raw_sales_data)
print(clean_data.head())
