import pandas as pd
import folium
from folium.plugins import HeatMap

df = pd.read_csv("firedataseasons.csv")

# converting datetime to format
df['acq_date'] = pd.to_datetime(df['acq_date'])


for year in range(2000, 2023):
    current_year_data = df[df['acq_date'].dt.year == year]
    
    #creating map
    m = folium.Map(location=[28.3949, 84.1240], zoom_start=5)

    #coordinatedata made
    locations = current_year_data[['latitude', 'longitude']].values.tolist()

    #making heatmap layers
    heatmap_layer = HeatMap(locations, radius=10)

    heatmap_layer.add_to(m)
    m.save(f"heatmap_{year}.html")
