import pandas as pd
import numpy as np

baseball_df = pd.read_csv("../dataset/baseball_stats.csv")


def calc_win_perc(wins, games_played):
    win_perc = wins / games_played
    return np.round(win_perc, 2)


win_percs_list = []

for i in range(len(baseball_df)):
    row = baseball_df.iloc[i]

    wins = row["W"]
    games_played = row["G"]

    win_perc = calc_win_perc(wins, games_played)

    win_percs_list.append(win_perc)

baseball_df["WP"] = win_percs_list

# pandas arrays
# Use the W array and G array to calculate win percentages
win_percs_np = calc_win_perc(baseball_df["W"].values, baseball_df["G"].values)

# Append a new column to baseball_df that stores all win percentages
baseball_df["WP"] = win_percs_np

print(baseball_df.head())
