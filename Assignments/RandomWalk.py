# Name:  Jose Ortiz
# Email: jose.ortiz60@myhunter.cuny.edu
# Date:  October 27, 2023
# A program that makes a turtle walk 100 times.

import turtle
from turtle import Screen #imported Screen so that the program doesn't exit on completion of execution
import random

trey = turtle.Turtle()
trey.speed(10) #speed of turtle

for i in range(100): #iterates 100 times
    trey.forward(10) #moves 10 steps forward
    a = random.randrange(0,360,1) #random.randrange(start, stop, step) step is the difference
    trey.right(a)

screen=Screen()
screen.exitonclick()