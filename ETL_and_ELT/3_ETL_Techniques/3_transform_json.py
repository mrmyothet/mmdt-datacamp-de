import json


def extract(file_path):
    with open(file_path, "r") as json_file:
        raw_data = json.load(json_file)
    return raw_data


file_path = "../data/nested_scores.json"
raw_testing_scores = extract(file_path)

raw_testing_scores_keys = []

# Iterate through the keys of the raw_testing_scores dictionary
for school_id in raw_testing_scores.keys():
    # Append each key to the raw_testing_scores_keys list
    raw_testing_scores_keys.append(school_id)

print(raw_testing_scores_keys[0:3])


raw_testing_scores_values = []

# Iterate through the values of the raw_testing_scores dictionary
for school_info in raw_testing_scores.values():
    raw_testing_scores_values.append(school_info)

print(raw_testing_scores_values[0:3])


raw_testing_scores_keys = []
raw_testing_scores_values = []

# Iterate through the values of the raw_testing_scores dictionary
for school_id, school_info in raw_testing_scores.items():
    raw_testing_scores_keys.append(school_id)
    raw_testing_scores_values.append(school_info)

print(raw_testing_scores_keys[0:3])
print(raw_testing_scores_values[0:3])

school = raw_testing_scores_values[2]
print("school dictionary", school)

# Parse the street_address from the dictionary
street_address = school.get("street_address")

# Parse the scores dictionary
scores = school.get("scores")

# Try to parse the math, reading and writing values from scores
math_score = scores.get("math", 0)
reading_score = scores.get("reading", 0)
writing_score = scores.get("writing", 0)

print(f"Street Address: {street_address}")
print(f"Math: {math_score}, Reading: {reading_score}, Writing: {writing_score}")
