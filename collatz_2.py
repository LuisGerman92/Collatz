#!/usr/bin/python3

# Collatz_2.py 
# This program takes an integer as input and
# generates all the Collatz numbers until it hits one.
# The numbers are then displayed to the terminal.

import sys, getopt
from helpers import dispBinary



n = int(sys.argv[1])
nn = n
print("Displaying the Collatz numbers for n=", n)

ints = 0
while(not (n == 1)):
    # even numbers
    if (n % 2 == 0):
        n = n/2
    else: # odd number
        n = 3*n+1
        
    ints += 1
    print(int(n), dispBinary(n))

print(nn, "has ", ints, " integers.")

