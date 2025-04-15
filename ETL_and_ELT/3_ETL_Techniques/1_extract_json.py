import pandas as pd
import json


def extract(file_path):
    # Read the JSON file into a DataFrame
    return pd.read_json(file_path, orient="records")


# Call the extract function with the appropriate path, assign to raw_testing_scores
file_path = "../data/testing_scores.json"
raw_testing_scores = extract(file_path)

# Output the head of the DataFrame
print(raw_testing_scores.head())

json.loads()
