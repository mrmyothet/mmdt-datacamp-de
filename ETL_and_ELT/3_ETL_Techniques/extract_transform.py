import pandas as pd
import json


def extract(file_path):
    with open(file_path, "r") as json_file:
        dt = json.load(json_file)

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
    raw_data.fillna(
        value={
            # Fill NaN values with column mean
            "math_score": raw_data["math_score"].mean(),
            "reading_score": raw_data["reading_score"].mean(),
            "writing_score": raw_data["writing_score"].mean(),
        },
        inplace=True,
    )
    return raw_data
