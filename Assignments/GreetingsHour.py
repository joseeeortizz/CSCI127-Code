# Name:  Jose Ortiz
# Email: jose.ortiz60@myhunter.cuny.edu
# Date:  October 19, 2023
# This program print the appropriate greeting based on the hour.

# Ask user for hour of the day
hour = int(input("Enter hour (in 24 hour time): "))

if 0 <= hour < 12:
    print("Good Morning")
elif 12 <= hour < 17:
    print("Good Afternoon")
else:
    print("Good Evening")