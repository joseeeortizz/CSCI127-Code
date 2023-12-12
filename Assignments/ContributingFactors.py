# Name:  Jose Ortiz
# Email: jose.ortiz60@myhunter.cuny.edu
# Date:  October 27, 2023
# A program lists the top three contributing factors for the primary vehicle of collisions

import pandas as pd

def read_collision_data(file_name):
    data = pd.read_csv(file_name)
    return data

def top_contributing_factors(data):
    contributing_factor_counts = data['CONTRIBUTING FACTOR VEHICLE 1'].value_counts()
    return contributing_factor_counts.head(3)

def main():
    file_name = input("Enter CSV file name: ")
    data = read_collision_data(file_name)
    top_factors = top_contributing_factors(data)
    print("Top three contributing factors for collisions:")
    print(top_factors)

if __name__ == "__main__":
    main()