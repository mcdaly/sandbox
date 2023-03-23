import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("data/goal_data.txt", delimiter="\t")

bins = range(0, 260000, 5000)

# plotting histograms
plt.hist(data['goal'][data["outcome"] == "successful"],
         label='success',
         bins=bins,
         # fill=False,
         color="green",
         edgecolor="green")

plt.hist(data['goal'][data["outcome"] == "failed"],
         label='fail',
         bins=bins,
         fill=False,
         edgecolor="red")

plt.legend(loc='upper right')
plt.title('Campaign Goals Success/Failures')
plt.show()

# plt.scatter(x=data['goal'],
#             y=data['outcome'])
# plt.show()
