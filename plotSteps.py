#!/usr/bin/python3

# plotSteps.py 
# This program takes an integer as input and
# computes the steps from 1 to n
# The numbers are then stored to a file.

import sys, getopt
from helpers import stepsTo1

# file to write results to
filename = "steps_data.txt"

# Check command-line argument
if (not len(sys.argv) == 2):
    print("Please provide a positive integer.")
    sys.exit()

n = int(sys.argv[1])

steps = []
for i in range(n):
    steps.append(stepsTo1(i+1))

# write results to plotData.gp
f = open(filename, "w")
f.write("# n   steps to reach 1")
for i in range(n):
    line = str(i+1) + " " + str(steps[i]) + '\n'
    f.write(line) 

f.close()
print("Finished writing to file. Please change xrange to ", n, " and yrange to ", max(steps), " in the plotData.gp file.")
