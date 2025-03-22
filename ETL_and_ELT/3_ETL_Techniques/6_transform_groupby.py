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


def transform(raw_data):
    # Use .loc[] to only return the needed columns
    raw_data = raw_data.loc[:, ["city", "math_score", "reading_score", "writing_score"]]

    # Group the data by city, return the grouped DataFrame
    grouped_data = raw_data.groupby(by=["city"], axis=0).mean()
    return grouped_data


file_path = "../data/nested_scores.json"
raw_data = extract(file_path)

raw_df = convert_to_df(raw_data)

clean_testing_scores = transform(raw_df)

# Print the head of the clean_testing_scores DataFrame
print(clean_testing_scores.head())
