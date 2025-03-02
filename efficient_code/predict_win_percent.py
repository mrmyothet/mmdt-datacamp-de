import pandas as pd
import numpy as np


baseball_df = pd.read_csv("../dataset/baseball_stats.csv")


def predict_win_perc(RS, RA):
    prediction = RS**2 / (RS**2 + RA**2)
    return np.round(prediction, 2)


win_perc_preds_loop = []

# Use a loop and .itertuples() to collect each row's predicted win percentage
# 13.6 ms +- 534 us per loop (mean +- std. dev. of 7 runs, 100 loops each)
for row in baseball_df.itertuples():
    runs_scored = row.RS
    runs_allowed = row.RA
    win_perc_pred = predict_win_perc(runs_scored, runs_allowed)
    win_perc_preds_loop.append(win_perc_pred)


# Apply predict_win_perc to each row of the DataFrame
# 31.4 ms +- 3.53 ms per loop (mean +- std. dev. of 7 runs, 10 loops each)
win_perc_preds_apply = baseball_df.apply(
    lambda row: predict_win_perc(row["RS"], row["RA"]), axis=1
)


# Calculate the win percentage predictions using NumPy arrays
# 22.7 us +- 1.22 us per loop (mean +- std. dev. of 7 runs, 10000 loops each)
win_perc_preds_np = predict_win_perc(baseball_df["RS"].values, baseball_df["RA"].values)
baseball_df["WP_preds"] = win_perc_preds_np
print(baseball_df.head())
