import json


def extract(file_path):
    with open(file_path, "r") as json_file:
        raw_data = json.load(json_file)
    return raw_data


file_path = "../data/nested_scores.json"
raw_testing_scores = extract(file_path)

# Print the raw_testing_scores
print(raw_testing_scores)
