# Name:  Jose Ortiz
# Email: jose.ortiz60@myhunter.cuny.edu
# Date:  October 27, 2023
# A template for a program that finds & marks the closest point.
# Modified by: Jose Ortiz

import folium
import pandas as pd

def getData():
    """
    Asks the user for the name of the CSV and
    Returns a dataframe of the contents.
    """
    csv_file = input("Enter CSV file name: ")
    df = pd.read_csv(csv_file)
    return df

def getColumnNames(df):
    """
    Asks the user for the exact name of the columns that
    contain the latitude and longitude from the given DataFrame df, and
    Returns those values as a tuple.
    """
    lat_col_name = input("Enter column name for latitude: ")
    lon_col_name = input("Enter column name for longitude: ")
    return (lat_col_name, lon_col_name)

def getLocale():
    """
    Asks the user for latitude and longitude of the user's current location and
    Returns those floating point numbers.
    """
    lat = float(input("Enter current latitude: "))
    lon = float(input("Enter current longitude: "))
    return lat, lon

def computeDist(x1, y1, x2, y2):
    """
    Computes the squared distance between two points (x1, y1) and (x2, y2) and
    Returns (x1-x2)^2 + (y1-y2)^2
    """
    return (x1 - x2) ** 2 + (y1 - y2) ** 2

############### Rest of the code remains the same
def dotAllPoints(cMap, df, latCol, lonCol):
    """
    Mark all points in the latCol, lonCol with dots (little circle markers)
    """
    for i, row in df.iterrows():
        folium.CircleMarker(location=[row[latCol], row[lonCol]], radius=4, color='red').add_to(cMap)


def markAndFindClosest(cMap, df, latCol, lonCol, cLat, cLon):
    """
    Goes through the list of points, marking each with a circle marker.
    Finds the closest point using the computeDist() function and
    Returns the lat and lon of closest point.
    """

    # Find closest marker:
    df['Dist'] = df[[latCol, lonCol]].apply(lambda row: computeDist(*row, cLat, cLon), axis=1)
    minRow = df[df['Dist'] == df['Dist'].min()]

    # Make a marker for the closest point:
    folium.Marker(location=[float(minRow[latCol]), float(minRow[lonCol])],
                  popup="Closest").add_to(cMap)
    # Make a marker for the starting point
    folium.Marker(location=[cLat, cLon],
                  popup="You Are Here",
                  icon=folium.Icon(color='red')).add_to(cMap)


def writeMap(cMap):
    """
    Writes the inputted map, cMap, to the file specified by the user.
    """
    outF = input('Enter output file: ')
    cMap.save(outfile=outF)


def main():
    dataF = getData()
    latColName, lonColName = getColumnNames(dataF)  # Pass dataF to getColumnNames
    lat, lon = getLocale()
    cityMap = folium.Map(location=[lat, lon], tiles='cartodbpositron', zoom_start=11)
    dotAllPoints(cityMap, dataF, latColName, lonColName)
    markAndFindClosest(cityMap, dataF, latColName, lonColName, lat, lon)
    writeMap(cityMap)

if __name__ == "__main__":
    main()