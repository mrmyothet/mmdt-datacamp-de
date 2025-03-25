import pandas as pd
import os


def print_df(df: pd.DataFrame):
    print(df.shape)
    print(df.columns)
    print(df.head())


# Extract function is already implemented for you
def extract(store_data, extra_data):
    extra_df = pd.read_parquet(extra_data)
    merged_df = store_data.merge(extra_df, on="index")
    return merged_df


# Create the transform() function with one parameter: "raw_data"
def transform(raw_data: pd.DataFrame):

    # print(raw_data["CPI"].unique())
    values = {
        "Weekly_Sales": raw_data["Weekly_Sales"].mean(),
        "CPI": raw_data["CPI"].mean(),
        "Unemployment": raw_data["Unemployment"].mean(),
    }

    raw_data.fillna(value=values, inplace=True)
    # print(raw_data["CPI"].unique())

    raw_data["Date"] = pd.to_datetime(raw_data["Date"], errors="coerce")
    raw_data["Month"] = raw_data["Date"].dt.month

    raw_data = raw_data.loc[raw_data["Weekly_Sales"] > 10000]

    selected_cols = [
        "Store_ID",
        "Month",
        "Dept",
        "IsHoliday",
        "Weekly_Sales",
        "CPI",
        "Unemployment",
    ]
    clean_data = raw_data[selected_cols]

    return clean_data


# Call the extract() function and store it as the "merged_df" variable
grocery_sales = pd.read_csv("grocery_sales.csv")
merged_df = extract(grocery_sales, "extra_data.parquet")
# print(merged_df)

# Call the transform() function and pass the merged DataFrame
clean_data = transform(merged_df)
print_df(clean_data)
