# Sisters Example from Spring 2015, #3
"""
def prob4(amy, beth):
    if amy > 4:
        print("Easy case")
        kate = -1
    else:
        print("Complex case")
        kate = helper(amy, beth)
    return (kate)


def helper(meg, jo):
    s = ""
    for j in range(meg):
        print(j, ": ", jo[j])
        if j % 2 == 0:
            s = s + jo[j]
            print("Building s:", s)
    return (s)


r = prob4(4, "city")
print("Return:  ", r)

r = prob4(2, "university")
print("Return:  ", r)
"""
#####################

def num2string(num):
    numString = {
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }

    return numString.get(num, "Invalid number")


###############

def setUp():
    #Create a new turtle
    newTurtle = turtle.Turtle()
    #Set the turtle so the pen is up newTurtle.penup()
    #Set the turtle so that the color is purple newTurtle.color("purple")
    #return the turtle with the setup
    return newTurtle
def getInput():
    #Ask the user for a value, convert it to
    #an int and store it in x
    x = int(input("Enter x: "))
    #Ask the user for another value, convert it to #an int and store it in y
    y = int(input("Enter y: "))
    #we can return two items in python
    return x, y
def markLocation(t, x, y):
    #t is the turtle given to the function
    #x and y are locations given to the function t.goto(x, y)
    t.stamp()
    #does not return a value

import turtle

def main():
    tess = setUp()

for i in range(5):
    x, y = getInput()
    markLocation(tess, x, y)

def setUp():
    newTurtle = turtle.Turtle()
    newTurtle.color("purple")
    newTurtle.penup()
    return (newTurtle)

def getInput():
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    return (x, y)
def markLocation(t, x, y):
    t.goto(x, y)
    t.stamp()

if __name__ == "__main__":
    main()