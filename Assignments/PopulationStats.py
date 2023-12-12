# Name:  Jose Ortiz
# Email: jose.ortiz60@myhunter.cuny.edu
# Date:  October 20, 2023
# This program calculates the average and maximum population for a given borough in New York City.

import pandas as pd

# Read the NYC historical population data.
pop = pd.read_csv('nycHistPop.csv', skiprows=5)

# Get the borough name from the user.
borough = input("Enter borough name: ")

# Check if the borough name is valid.
if borough not in pop.columns:
    print("Invalid borough name.")
else:
    # Compute the average and maximum population for the borough.
    average = pop[borough].mean()
    maximum = pop[borough].max()

    # Print the average and maximum population for the borough.
    print("Average population:", average)
    print("Maximum population:", maximum)