import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt

banking = pd.read_csv("../dataset/banking_dirty.csv")
print(banking)

# Print number of missing values in banking
print(banking.isna().sum())

# Visualize missingness matrix
msno.matrix(banking)
plt.show()

# Isolate missing and non missing values of inv_amount
missing_investors = banking[banking["inv_amount"].isna()]
investors = banking[~banking["inv_amount"].isna()]

# Sort banking by age and visualize
banking_sorted = banking.sort_values(by="age")
msno.matrix(banking_sorted)
plt.show()
