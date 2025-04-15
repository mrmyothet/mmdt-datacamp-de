import pandas as pd
import json


def extract(file_path):
    with open(file_path, "r") as json_file:
        raw_data = json.load(json_file)
    return raw_data


def convert_to_df(dt: dict):
    lst = []
    # Loop through each of the dictionary key-value pairs
    for key, value in dt.items():
        lst.append(
            [
                key,
                value.get("street_address"),  # Pull the "street_address"
                value.get("city"),
                value.get("scores").get("math", 0),
                value.get("scores").get("reading", 0),
                value.get("scores").get("writing", 0),
            ]
        )

    # Create a DataFrame from the normalized_testing_scores list
    normalized_data = pd.DataFrame(lst)

    # Set the column names
    normalized_data.columns = [
        "school_id",
        "street_address",
        "city",
        "math_score",
        "reading_score",
        "writing_score",
    ]

    normalized_data = normalized_data.set_index("school_id")
    return normalized_data


def find_street_name(row):
    # Split the street_address by spaces
    split_street_address = row["street_address"].split(" ")

    # Remove the number
    street_number = split_street_address[0]
    try:
        int(street_number)
    except ValueError:
        return row["street_address"]

    without_street = " ".join(split_street_address[1:])
    return without_street


def transform(raw_data):
    # Use the apply function to extract the street_name from the street_address
    raw_data["street_name"] = raw_data.apply(
        # Pass the correct function to the apply method
        find_street_name,
        axis=1,
    )
    return raw_data


file_path = "/home/myothet/myothet/mmdt-datacamp-de/ETL_and_ELT/data/nested_scores.json"
raw_data = extract(file_path)

raw_df = convert_to_df(raw_data)

clean_testing_scores = transform(raw_df)

# Print the head of the clean_testing_scores DataFrame
print(clean_testing_scores.head())
