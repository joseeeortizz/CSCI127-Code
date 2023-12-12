# Name:  Jose Ortiz
# Email: jose.ortiz60@myhunter.cuny.edu
# Date:  October 27, 2023
# A program that that asks the user to enter a string. If the user enters an empty string, your program should continue prompting the user for a new string until they enter a non-empty string.

while True:
    user_string = input("Enter a non-empty string: ")
    if user_string == "":
        print("That was empty. Try again.")
    else:
        print(f"You entered: {user_string}")
        break