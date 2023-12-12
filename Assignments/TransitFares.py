# Name:  Jose Ortiz
# Email: jose.ortiz60@myhunter.cuny.edu
# Date:  October 27, 2023
# This program  takes as two parameters: the zone and the ticket type, and returns the Long Island Railroad fare.

def computeFare(zone, ticketType):
    """
    Takes as two parameters: the zone and the ticket type.
    Returns the LIRR Transit fare based on the given zone and ticket type.
    """
    if zone == 1:
        if ticketType == "peak":
            return 8.75
        elif ticketType == "off-peak":
            return 6.25
    elif zone in [2, 3]:
        if ticketType == "peak":
            return 10.25
        elif ticketType == "off-peak":
            return 7.50
    elif zone == 4:
        if ticketType == "peak":
            return 12.00
        elif ticketType == "off-peak":
            return 8.75
    elif zone in [5, 6, 7]:
        if ticketType == "peak":
            return 13.50
        elif ticketType == "off-peak":
            return 9.75
    else:
        return -1  # Return a negative number for zones greater than 8

def main():
    z = int(input('Enter the number of zones: '))
    t = input('Enter the ticket type (peak/off-peak): ').lower()
    fare = computeFare(z, t)
    if fare == -1:
        print('Zone is greater than 8. The fare cannot be calculated.')
    else:
        print('The fare is', fare)

# Allow script to be run directly:
if __name__ == "__main__":
    main()
