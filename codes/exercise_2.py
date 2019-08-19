import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# It might be needed to change the path according to your file location.
data = pd.read_excel("../dataset/LaptopSales.xls")
data["Lat-Lon"] = data["OS X Store"].map(str) + "," + data["OS Y Store"].map(str)
means = data.groupby(["Lat-Lon"]).mean()[["Retail Price"]]

fig, (ax, bx) = plt.subplots(1, 2, figsize=(12, 6))
ax.bar(means.index, means["Retail Price"])
ax.tick_params(axis='x', rotation=90)
ax.set_xlabel("Store's coordinate [Lat, Lon]")
ax.set_ylim(470, 500)
ax.set_ylabel("Average laptop price [USD]")
ax.set_title("Average price of laptop in different stores")

data.boxplot(column=['Retail Price'], by=['Lat-Lon'], ax=bx)
bx.tick_params(axis='x', rotation=90)

fig.suptitle("")
fig.tight_layout()
plt.show()
