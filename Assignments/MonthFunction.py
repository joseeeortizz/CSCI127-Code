# Name:  Jose Ortiz
# Email: jose.ortiz60@myhunter.cuny.edu
# Date:  October 26, 2023
# A program that uses functions to print out months.


def monthString(monthNum):
    """
    Takes as input a number, monthNum, and
    returns the corresponding month name as a string.
    Example: monthString(1) returns "January".
    Assumes that input is an integer ranging from 1 to 12
    """

    # List of month names
    months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]

    # Check if the input is within the valid range
    if 1 <= monthNum <= 12:
        # Subtract 1 from monthNum to get the correct index in the list
        monthString = months[monthNum - 1]
    else:
        monthString = "Invalid month number"

    return monthString

def main():
    n = int(input('Enter the number of the month: '))
    mString = monthString(n)
    print('The month is', mString)

# Allow script to be run directly:
if __name__ == "__main__":
    main()
