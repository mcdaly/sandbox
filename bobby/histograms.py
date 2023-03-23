import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data/goal_data.txt", delimiter="\t")

bins = range(0, 260000, 5000)

success_df = data[data["outcome"] == "successful"]
failed_df = data[data["outcome"] == "failed"]

# plotting histograms
plt.hist(success_df['goal'],
         label='success',
         bins=bins,
         # fill=False,
         color="green",
         edgecolor="green")

plt.hist(failed_df['goal'],
         label='fail',
         bins=bins,
         fill=False,
         edgecolor="red")

plt.legend(loc='upper right')
plt.title('Campaign Goals Success/Failures')
plt.show()
