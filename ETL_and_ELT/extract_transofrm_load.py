import pandas as pd


def extract(file_name):
    return pd.read_csv(file_name)


def transform(data_frame):
    # Filter the data_frame to only incude a subset of columns
    return data_frame.loc[:, ["industry_name", "number_of_firms"]]


def load(data_frame, file_name):
    # Write the data_frame to a CSV
    data_frame.to_csv(file_name)


extracted_data = extract(file_name="data/raw_industry_data.csv")
transformed_data = transform(data_frame=extracted_data)

# Pass the transformed_data DataFrame to the load() function
load(data_frame=transformed_data, file_name="data/number_of_firms.csv")
