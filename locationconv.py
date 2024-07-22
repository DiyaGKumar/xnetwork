# Converts locations of all users to long/lat for plotting
import csv
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderUnavailable
import time

# Initialize the geocoder
geolocator = Nominatim(user_agent="my_app")

def get_lat_lon(location):
    try:
        # Geocode the location
        location = geolocator.geocode(location)
        if location:
            return (location.latitude, location.longitude)
    except (GeocoderTimedOut, GeocoderUnavailable):
        # If the geocoder times out, wait and try again
        time.sleep(1)
        return get_lat_lon(location)
    return None

# Read the refined data
refined_data = []
with open('refined.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    for row in reader:
        refined_data.append(row)

# Convert locations to lat/long and write to new CSV
with open('locations_with_coordinates.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Location', 'Latitude', 'Longitude'])  # Write header

    for name, location in refined_data:
        print(f"Processing: {name} - {location}")
        coordinates = get_lat_lon(location)
        if coordinates:
            lat, lon = coordinates
            writer.writerow([name, location, lat, lon])
        else:
            print(f"Could not find coordinates for {location}")

print("Conversion complete. Data saved to 'locations_with_coordinates.csv'")