import pandas as pd
from extract_transform import extract, transform
import sqlalchemy


file_path = "/home/myothet/myothet/mmdt-datacamp-de/ETL_and_ELT/data/nested_scores.json"

raw_df = extract(file_path)
clean_testing_scores = transform(raw_df)

# Print the head of the clean_testing_scores DataFrame
print(clean_testing_scores.head())


# Update the connection string, create the connection object to the schools database
db_engine = sqlalchemy.create_engine(
    "postgresql+psycopg2://postgres:postgres@localhost:5433/schools"
)

# Write the DataFrame to the scores table
clean_testing_scores.to_sql(
    name="scores", con=db_engine, index=False, if_exists="replace"
)
