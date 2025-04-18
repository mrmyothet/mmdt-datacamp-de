#!/usr/bin/env python
# coding: utf-8


# Import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV and assign it to the variable data
data = pd.read_csv("../dataset/vt_tax_data_2016.csv")

# View the first few lines of data
print(data.head())


# Load TSV using the sep keyword argument to set delimiter
# data = pd.read_csv('vt_tax_data_2016.tsv', sep='\t')

# Plot the total number of tax returns by income group
# counts = data.groupby("agi_stub").N1.sum()
# counts.plot.bar()
# plt.show()


# Plot the total number of tax returns by income group
counts = data.groupby("agi_stub").N1.sum()
counts.plot.bar()
plt.show()
