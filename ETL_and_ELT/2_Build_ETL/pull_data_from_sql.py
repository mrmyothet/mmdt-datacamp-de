import sqlalchemy
import pandas as pd


def extract():
    connection_uri = "postgresql+psycopg2://repl:password@localhost:5432/sales"
    db_engine = sqlalchemy.create_engine(connection_uri)
    raw_data = pd.read_sql("SELECT * FROM sales WHERE quantity_ordered = 1", db_engine)

    # Print the head of the DataFrame
    print(raw_data.head())

    # Return the extracted DataFrame
    return raw_data


# Call the extract() function
raw_sales_data = extract()
