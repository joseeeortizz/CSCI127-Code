# Name:  Jose Ortiz
# Email: jose.ortiz60@myhunter.cuny.edu
# Date:  November 21, 2023
# Sample program that loops through numbers 0, 5, 10, ..., 50

ADDI $s0, $zero, 0 #set s0 as 0 s0=0+0=0
ADDI $s1, $zero, 50 #set s1 as 50 s1=0+50=s0
AGAIN: ADDI $s0, $s0, 5 #increment 5 s0=s0+5
BEQ $s0, $s1 , DONE #if so=s1 means s0=50 go to done(BEQ=Branch when equal)
J AGAIN #else continue in loop
DONE: