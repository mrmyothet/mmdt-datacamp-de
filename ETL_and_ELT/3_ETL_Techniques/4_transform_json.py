import json
import pandas as pd


def extract(file_path):
    with open(file_path, "r") as json_file:
        raw_data = json.load(json_file)
    return raw_data


file_path = "../data/nested_scores.json"
raw_testing_scores = extract(file_path)

normalized_testing_scores = []

# Loop through each of the dictionary key-value pairs
for school_id, school_info in raw_testing_scores.items():
    normalized_testing_scores.append(
        [
            school_id,
            school_info.get("street_address"),  # Pull the "street_address"
            school_info.get("city"),
            school_info.get("scores").get("math", 0),
            school_info.get("scores").get("reading", 0),
            school_info.get("scores").get("writing", 0),
        ]
    )

# print(normalized_testing_scores)

# Create a DataFrame from the normalized_testing_scores list
normalized_data = pd.DataFrame(normalized_testing_scores)

# Set the column names
normalized_data.columns = [
    "school_id",
    "street_address",
    "city",
    "avg_score_math",
    "avg_score_reading",
    "avg_score_writing",
]

normalized_data = normalized_data.set_index("school_id")
print(normalized_data.head())
