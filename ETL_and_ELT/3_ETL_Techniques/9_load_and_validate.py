import pandas as pd
import sqlalchemy
from extract_transform import extract


# def extract(file_path):
#     return pd.read_json(file_path)


def transform(raw_data):
    clean_data = raw_data.dropna()

    clean_data["total_score"] = clean_data.loc[
        :, ["math_score", "reading_score", "writing_score"]
    ].sum(axis=1)

    clean_data["city_rank"] = clean_data.groupby("city")["total_score"].rank(
        method="dense", ascending=False
    )

    clean_data = clean_data.drop("total_score", axis=1)
    return clean_data


def load(clean_data, con_engine):
    # Store the data in the schools database
    clean_data.to_sql(
        name="scores_by_city",
        con=con_engine,
        if_exists="replace",  # Make sure to replace existing data
        index=True,
        index_label="school_id",
    )


file_path = "/home/myothet/myothet/mmdt-datacamp-de/ETL_and_ELT/data/nested_scores.json"
conn_str = "postgresql+psycopg2://postgres:postgres@localhost:5433/schools"

raw_df = extract(file_path)
transformed_df = transform(raw_df)

db_engine = sqlalchemy.create_engine(conn_str)
load(transformed_df, db_engine)


# Call query the data in the scores_by_city table, check the head of the DataFrame
to_validate = pd.read_sql("SELECT * FROM scores_by_city", con=db_engine)
print(to_validate.head())
