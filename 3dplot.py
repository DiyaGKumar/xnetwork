# Plots users on a 3D Globe 
import pandas as pd
import plotly.express as px

# Read the CSV file
df = pd.read_csv('locations_with_coordinates.csv')

# Create the 3D globe
fig = px.scatter_geo(df,
                     lat="Latitude",
                     lon="Longitude",
                     hover_name="Name",
                     hover_data=["Location"],
                     projection="orthographic")

# Customize the layout
fig.update_geos(
    showcoastlines=True,
    coastlinecolor="RebeccaPurple",
    showland=True,
    landcolor="LightGreen",
    showocean=True,
    oceancolor="LightBlue",
    showlakes=True,
    lakecolor="Blue",
    showcountries=True,
    countrycolor="Black"
)

# Adjust the layout
fig.update_layout(height=800, margin={"r":0,"t":0,"l":0,"b":0})

# Show the map
fig.show()

# Optionally, save the map as an HTML file
fig.write_html("followers_3d_globe.html")