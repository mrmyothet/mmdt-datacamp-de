from pipeline_utils import extract, transform
import pandas as pd
import pytest


def transform_industry_name(raw_data):
    # Find average taxable income for each business type.
    raw_data["average_taxable_income"] = (
        raw_data["total_taxable_income"] / raw_data["number_of_firms"]
    )

    # Only keep records with average_taxable_income > 100.
    clean_data = raw_data.loc[raw_data["average_taxable_income"] > 100, :]

    # Set the index to the industry_name.
    clean_data.set_index("industry_name", inplace=True)

    # Return the clean DataFrame.
    return clean_data


def test_transformed_data():
    raw_tax_data = extract("../data/raw_tax_data.csv")
    clean_tax_data = transform_industry_name(raw_tax_data)

    # Assert that the transform function returns a pd.DataFrame
    assert isinstance(clean_tax_data, pd.DataFrame)

    # Assert that the clean_tax_data DataFrame has more columns than the raw_tax_data DataFrame
    assert len(clean_tax_data.columns) < len(raw_tax_data.columns)


# Create a pytest fixture
@pytest.fixture()
def raw_tax_data():
    raw_data = extract("../data/raw_tax_data.csv")

    # Return the raw DataFrame
    return raw_data


def transform(raw_data):
    raw_data["tax_rate"] = (
        raw_data["total_taxes_paid"] / raw_data["total_taxable_income"]
    )
    raw_data.set_index("industry_name", inplace=True)
    return raw_data


# Define a pytest fixture
@pytest.fixture()
def clean_tax_data():
    raw_data = pd.read_csv("../data/raw_tax_data.csv")

    # Transform the raw_data, store in clean_data DataFrame, and return the variable
    clean_data = transform(raw_data)
    return clean_data


# Pass the fixture to the function
def test_tax_rate(clean_tax_data):
    # Assert values are within the expected range
    assert (
        clean_tax_data["tax_rate"].max() <= 1 and clean_tax_data["tax_rate"].min() >= 0
    )
