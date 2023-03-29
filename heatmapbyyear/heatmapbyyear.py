import pandas as pd
import folium
from folium.plugins import HeatMap

# read the CSV file
df = pd.read_csv("firedataseasons.csv")

# convert the acq_date column to datetime format
df['acq_date'] = pd.to_datetime(df['acq_date'])

# loop through each year from 2000 to 2022
for year in range(2000, 2023):
    # filter the data for the current year
    current_year_data = df[df['acq_date'].dt.year == year]
    
    # create a map with folium
    m = folium.Map(location=[28.3949, 84.1240], zoom_start=5)

    # create a list of latitudes and longitudes
    locations = current_year_data[['latitude', 'longitude']].values.tolist()

    # create a heatmap layer
    heatmap_layer = HeatMap(locations, radius=10)

    # add the heatmap layer to the map
    heatmap_layer.add_to(m)

    # save the output to an HTML file
    m.save(f"heatmap_{year}.html")
