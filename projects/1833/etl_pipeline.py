import pandas as pd
import os


def print_df(df: pd.DataFrame):
    print(df.shape)
    print(df.columns)
    print(df.head())


def extract(store_data, extra_data):
    extra_df = pd.read_parquet(extra_data)
    merged_df = store_data.merge(extra_df, on="index")
    return merged_df


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


def avg_weekly_sales_per_month(clean_data: pd.DataFrame):
    agg_df = clean_data[["Month", "Weekly_Sales"]]

    agg_df = agg_df.groupby(["Month"])["Weekly_Sales"].mean().reset_index().round(2)

    agg_df.rename(columns={"Weekly_Sales": "Avg_Sales"}, inplace=True)

    return agg_df


def load(
    full_data: pd.DataFrame,
    full_data_file_path: str,
    agg_data: pd.DataFrame,
    agg_data_file_path: str,
):
    full_data.to_csv(full_data_file_path, index=False)
    agg_data.to_csv(agg_data_file_path, index=False)


def validation(file_path):
    if os.path.exists(file_path):
        print(file_path)
    else:
        raise FileNotFoundError


# Call the extract() function and store it as the "merged_df" variable
grocery_sales = pd.read_csv("grocery_sales.csv")
merged_df = extract(grocery_sales, "extra_data.parquet")
# print(merged_df)

# Call the transform() function and pass the merged DataFrame
clean_df = transform(merged_df)
# print(clean_df)

# Call the avg_weekly_sales_per_month() function and pass the cleaned DataFrame
agg_df = avg_weekly_sales_per_month(clean_df)
# print_df(agg_df)

# Call the load() function and pass the cleaned and aggregated DataFrames with their paths
clean_data_file_path = "clean_data.csv"
agg_data_file_path = "agg_data.csv"
load(clean_df, clean_data_file_path, agg_df, agg_data_file_path)

# Call the validation() function and pass first, the cleaned DataFrame path, and then the aggregated DataFrame path
validation(clean_data_file_path)
validation(agg_data_file_path)
