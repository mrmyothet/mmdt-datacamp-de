import pandas as pd


def extract(file_name):
    print(f"Extracting data from {file_name}.")
    return pd.read_csv(file_name)


# Complete building the transform() function
def transform(source_table, target_table):
    data_warehouse.execute(
        f"""
  CREATE TABLE {target_table} AS
      SELECT
          CONCAT("Product ID: ", product_id),
          quantity * price
      FROM {source_table};
  """
    )


def load(data_frame, target_table):
    print(f"Loading cleaned data to {target_table}.")
