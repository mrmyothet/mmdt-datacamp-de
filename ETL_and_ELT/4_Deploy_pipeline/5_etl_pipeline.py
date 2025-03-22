import logging
from pipeline_utils import extract, transform, load


logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)

try:
    raw_tax_data = extract("../data/raw_tax_data.csv")
    clean_tax_data = transform(raw_tax_data)
    load(clean_tax_data, "../data/clean_tax_data.parquet")

    logging.info(
        "Successfully extracted, transformed and loaded data."
    )  # Log a success message.

except Exception as e:
    logging.error(f"Pipeline failed with error: {e}")  # Log failure message
