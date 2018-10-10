#!/usr/bin/python3

# Collatz.py 
# This program takes an integer as input and
# generates all the Collatz numbers until it hits one.
# The numbers are then displayed to the terminal.

import sys, getopt
from helpers import dispBinary

# Check command-line argument
if (not len(sys.argv) == 2):
    print("Please provide a positive integer.")
    sys.exit()


n = int(sys.argv[1])
nn = n
print("Displaying the Collatz numbers for n=", n)

ints = 0
odds = []
while(not (n == 1)):
    # even number
    if (n % 2 == 0):
        n = n/2
    else: # odd number
        odds.append(n)
        n = 3*n+1
        
    ints += 1
    print(int(n))

print(nn, "has ", ints, " integers.")
