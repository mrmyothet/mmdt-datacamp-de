# Re-run this cell
import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
schools.head()

# Start coding here...

# Which schools are best for math?
best_math_schools = schools[schools["average_math"] >= 640][
    ["school_name", "average_math"]
].sort_values("average_math", ascending=False)

# Calculate total_SAT per school
schools["total_SAT"] = (
    schools["average_math"] + schools["average_reading"] + schools["average_writing"]
)

# Who are the top 10 performing schools?
top_10_schools = schools.sort_values("total_SAT", ascending=False)[
    ["school_name", "total_SAT"]
].head(10)

# Which NYC borough has the highest standard deviation for total_SAT?
boroughs = (
    schools.groupby("borough")["total_SAT"].agg(["count", "mean", "std"]).round(2)
)

# Filter for max std and make borough a column
largest_std_dev = boroughs[boroughs["df = schools.groupby("borough")["total_SAT"].agg(["count", "mean", "std"]).round(2)

largest_std_dev = df[df["std"] == df["std"].max()]

new_columns = {
    "borough":"borough",
    "count": "num_schools", 
    "mean": "average_SAT",
    "std":"std_SAT", 
}

largest_std_dev = largest_std_dev.rename(columns=new_columns)

largest_std_dev"] == boroughs["std"].max()]

# Rename the columns for clarity
largest_std_dev = largest_std_dev.rename(
    columns={"count": "num_schools", "mean": "average_SAT", "std": "std_SAT"}
)

# Optional: Move borough from index to column
largest_std_dev.reset_index(inplace=True)