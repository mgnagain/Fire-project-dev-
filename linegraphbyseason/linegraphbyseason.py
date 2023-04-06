import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('firedataseasons.csv')

#grouping data
grouped = df.groupby(['year', 'Season']).size().reset_index(name='counts')

#pivoting
pivoted = grouped.pivot(index='Season', columns='year', values='counts')

#plotstyle
plt.style.use('ggplot')

#23 diff colors were needed so defined all colors here
colors = ['blue', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'olive', 'cyan', 'magenta', 'yellow', 'orange', 'maroon', 'teal', 'navy', 'coral', 'indigo', 'crimson', 'chocolate', 'lime', 'turquoise', 'gold', 'steelblue']

#creating plot
for i, col in enumerate(pivoted.columns):
    pivoted[col].plot(kind='line', marker='o', figsize=(10,6), color=colors[i])

plt.xlabel('Season')

plt.ylabel('Number of fires')

plt.yticks(range(0, 8000, 250))

plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))

plt.title('Number of fires by season and year')

plt.savefig("linegraphbyseason.jpeg")

plt.show()
