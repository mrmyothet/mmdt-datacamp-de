import pandas as pd
import requests
from pandas import json_normalize

url = "https://raw.githubusercontent.com/owid/covid-19-data/refs/heads/master/public/data/latest/owid-covid-latest.json"
response = requests.get(url)
data = response.json()

result_df = pd.DataFrame()

for key in data.keys():
    row = data[key]
    row_df = pd.json_normalize(row)
    row_df["country_code"] = key
    result_df = pd.concat([result_df, row_df], ignore_index=True)

assert result_df.shape == (247, 67), "dataframe is incorrect shape"

url_countries = "https://raw.githubusercontent.com/dr5hn/countries-states-cities-database/refs/heads/master/json/countries.json"
response_contries = requests.get(url_countries)
raw_data_countries = response_contries.json()
df_countries = pd.json_normalize(raw_data_countries)

df_countries = df_countries[["iso3", "capital"]]

merge_df = result_df.merge(df_countries, left_on="country_code", right_on="iso3")

selected_cols = [
    "continent",
    "location",
    "last_updated_date",
    "total_cases",
    "new_cases",
    "new_cases_smoothed",
    "total_deaths",
    "new_deaths",
    "new_deaths_smoothed",
    "total_cases_per_million",
    "iso3",
    "capital",
]

processed_df = merge_df[selected_cols]
print("shape of covid_19_data", processed_df.shape)
