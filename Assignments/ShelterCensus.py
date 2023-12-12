# Name:  Jose Ortiz
# Email: jose.ortiz60@myhunter.cuny.edu
# Date:  October 20, 2023
# This program prints the shelter census from NYC reports.

import pandas as pd
import matplotlib.pyplot as plt

#Taking input from user
input_file = input('Enter name of input file: ')
output_file = input('Enter name of output file: ')
homeless = pd.read_csv(input_file)
#Add a new column 'Fraction Children'to the dataframe
#Fraction Children = Total Children in shelter / Total Individuals in Shelter
homeless['Fraction Children'] = homeless['Total Children in Shelter'] / homeless['Total Individuals in Shelter']
#plot the fraction of Children
homeless.plot(x = "Date of Census", y = "Fraction Children")
plt.show()
#plt.savefig saves the file to given name
plt.savefig(output_file)