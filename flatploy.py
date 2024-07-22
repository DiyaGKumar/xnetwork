# Plots all users on 2D Map 
import pandas as pd
import plotly.express as px

# Read the CSV file
df = pd.read_csv('locations_with_coordinates.csv')

# Create the map
fig = px.scatter_mapbox(df, 
                        lat="Latitude", 
                        lon="Longitude", 
                        hover_name="Name", 
                        hover_data=["Location"],
                        zoom=1)

# Use OpenStreetMap style
fig.update_layout(mapbox_style="open-street-map")

# Adjust the layout
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

# Show the map 
fig.show()

# Optionally, save the map as an HTML file
fig.write_html("followers_map.html")