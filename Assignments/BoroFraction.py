# Name:  Jose Ortiz
# Email: jose.ortiz60@myhunter.cuny.edu
# Date:  October 20, 2023
# This program prints the fraction of a given borough.

import pandas as pd
import matplotlib.pyplot as plt

pop = pd.read_csv('nycHistPop.csv',skiprows=5)

borough=input('Enter borough name: ')
file=input('Enter file name: ')

pop['Fraction'] = pop[borough]/pop['Total']

pop.plot(x='Year',y='Fraction')
fig=plt.gcf()
fig.savefig(file)