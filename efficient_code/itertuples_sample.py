import pandas as pd

rangers_df = pd.read_csv("../dataset/baseball_stats.csv")
yankees_df = pd.read_csv("../dataset/baseball_stats.csv")
# Loop over the DataFrame and print each row's Index, Year and Wins (W)
print(rangers_df.head())

for row in rangers_df.itertuples():
    i = row.Index
    year = row.Year
    wins = row.W

    # Check if rangers made Playoffs (1 means yes; 0 means no)
    if row.Playoffs == 1:
        print(i, year, wins)

run_diffs = []

print(yankees_df.head())

# Loop over the DataFrame and calculate each row's run differential
for row in yankees_df.itertuples():

    runs_scored = row.RS
    runs_allowed = row.RA


def calc_run_diff(runs_scored, runs_allowed):

    run_diff = runs_scored - runs_allowed

    return run_diff


run_diffs = []

# Loop over the DataFrame and calculate each row's run differential
for row in yankees_df.itertuples():

    runs_scored = row.RS
    runs_allowed = row.RA

    run_diff = calc_run_diff(runs_scored, runs_allowed)

    if run_diff == 210 or run_diff == 309 or run_diff == 503 or run_diff == 315:
        print(year, runs_scored, runs_allowed, run_diff)
    run_diffs.append(run_diff)

    run_diffs.append(run_diff)

# Append new column
yankees_df["RD"] = run_diffs
print(yankees_df)
