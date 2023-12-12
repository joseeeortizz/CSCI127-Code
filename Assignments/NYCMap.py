# Name:  Jose Ortiz
# Email: jose.ortiz60@myhunter.cuny.edu
# Date:  October 27, 2023
# This program uses folium to make a map of New York City.

import folium

# Create a map centered at (40.75, -74.125)
nycMap = folium.Map(location=[40.75, -74.125], zoom_start=12)

# Add a marker for the main campus of Hunter College
folium.Marker([40.774, -73.950], popup='Hunter College Main Campus').add_to(nycMap)

# Save the map as an HTML file
nycMap.save('nycMap.html')