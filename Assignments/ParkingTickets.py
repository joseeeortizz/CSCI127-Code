# Name:  Jose Ortiz
# Email: jose.ortiz60@myhunter.cuny.edu
# Date:  October 24, 2023
# This program counts which cars got the most parking tickets

#Import pandas for reading and analyzing CSV data:
import pandas as pd

csvFile = input('Enter CSV file name: ')         #Name of the CSV file
attribute = input('Enter attribute: ')         #Attribute to search by

tickets = pd.read_csv(csvFile)     #Read in the file to a dataframe

# Check if the attribute exists in the dataframe
if attribute in tickets.columns:
    print("The 10 worst offenders are:")
    print(tickets[attribute].value_counts()[:10]) #Print out the dataframe
else:
    print("The attribute does not exist in the file.")