import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("../data/goal_data.txt", delimiter="\t")

success_df = data[data["outcome"] == "successful"]
failed_df = data[data["outcome"] == "failed"]

# Calculate metrics for campaigns
sigma = 1
names = ["successful", "failed"]
averages = [np.average(success_df["goal"]), np.average(failed_df["goal"])]
medians = [np.median(success_df["goal"]), np.median(failed_df["goal"])]
stdev = [np.std(success_df["goal"])*sigma, np.std(failed_df["goal"])*sigma]

print(f"          Successful    Failed")
print(f"Averages: {averages[0]:8.2f}      {averages[1]:8.2f}")
print(f"Medians : {medians[0]:8.2f}      {medians[1]:8.2f}")
print(f"Std Dev : {stdev[0]:8.2f}      {stdev[1]:8.2f}")

# Generate scatter plot with error bars
plt.scatter(x=data['goal'],
            y=data['outcome'])
plt.errorbar(medians, names, xerr=stdev, fmt="*", color='red')
plt.show()
