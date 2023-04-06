import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("firedataseasons.csv")

df = df[(df["year"] >= 2000) & (df["year"] <= 2022)]

counts = df.groupby(["year", "month"]).size()

counts = counts.unstack(level=0)

counts.plot(kind="line", figsize=(10, 5))

plt.title("Number of Fires by Year and Month (2000-2022)")
plt.xlabel("Month")
plt.ylabel("Number of Fires")

plt.xticks(range(1, 13))
plt.yticks(range(0, 7000, 250))

plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.savefig("linegraphbyyear.jpeg")

plt.show()
