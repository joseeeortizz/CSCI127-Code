# Name:  Jose Ortiz
# Email: jose.ortiz60@myhunter.cuny.edu
# Date:  October 27, 2023
# This program creates a map with markers for all the traffic collisions from the input file.

import folium
import pandas as pd

inF = input('Enter input filename: ')
outF = input('Enter output filename: ')

collisions = pd.read_csv(inF)
collisions["LATITUDE"] = collisions["LATITUDE"].fillna(0)
collisions["LONGITUDE"] = collisions["LONGITUDE"].fillna(0)

mapCrash = folium.Map(location=[40.768731, -73.964915])

for index, row in collisions.iterrows():
    if row['LATITUDE'] != 0 and row['LONGITUDE'] != 0:
        # Create a marker for each collision and add it to the map
        folium.Marker(
            location=[row['LATITUDE'], row['LONGITUDE']],
            popup=f"Collision Date: {row['DATE']}",
            icon=folium.Icon(color='red')
        ).add_to(mapCrash)

mapCrash.save(outfile=outF)
