#creating bar graphs to display number of fires happening each season in each year
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("firedataseasons.csv")

#Grouping data by year and season and counting the number of fires in each
season_counts = df.groupby(["year", "Season"]).size()

#Making the index
index = []
for year in range(2000, 2023):
    year_data = season_counts.loc[year]
    season_data = year_data.reindex(["Winter", "Spring", "Summer", "Fall"]).fillna(0)
    index.extend(season_data.values)

#Making the Bar Graph
for year in range(2000, 2023):
    year_data = season_counts.loc[year]
    season_data = year_data.reindex(["Winter", "Spring", "Summer", "Fall"]).fillna(0)
    plt.bar(season_data.index, season_data.values)
    plt.title(f"Fires in Nepal - {year}")
    plt.xlabel("Season")
    plt.ylabel("Number of Fires")
    #naming the bars
    for i, v in enumerate(season_data.values):
        plt.text(i, v+50, str(v), color='blue', fontweight='bold', ha='center')
    #Generating index box
    box_text = f"Index:\nWinter - {index[(year-2000)*4]:.0f}\nSpring - {index[(year-2000)*4+1]:.0f}\nSummer - {index[(year-2000)*4+2]:.0f}\nFall - {index[(year-2000)*4+3]:.0f}"
    plt.text(0.02, 0.9, box_text, transform=plt.gca().transAxes, fontsize=10, bbox=dict(facecolor='white', edgecolor='gray', boxstyle='round'))
    #Self explanatory ig
    plt.savefig(f"fires_nepal_{year}.png")
    plt.clf()

#print the index(using to debug in terminal)
print("Index that denotes the accurate number of fires for each season:")
print(index)

