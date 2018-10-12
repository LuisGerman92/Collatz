#!/usr/bin/python3

# helpers.py
# contains helper functions related to the Collatz conjecture problem

import sys, getopt
from math import log2
import fractions

def int2binaryTree(n):
    if n==1:
        return 'X'
    out = ''
    numOfBits = int(log2(n))
    binaryNum = dispBinary(n-pow(2,numOfBits))
    for i in range(numOfBits-len(binaryNum)):
        # append ceros
        out += '0'
    # append binary representation of number
    out += binaryNum
    # convert every 0 to 'L' and every 1 to 'R'
    lr_out = ''
    for char in out:
        if char == '0':
            lr_out += 'L'
        if char == '1':
            lr_out += 'R'
    return lr_out


def dispBinary(n):
    if n==0:
        return ''
    out = ''
    while (not (n==1)):
        if (n%2 == 1):
            out += '1'
        else:
            out += '0'
        n = int(n/2)
    out += '1'
    return out[::-1]


# perform over n the transformations as specified by the sequence seq
def I_str(n,seq):
    # convert number from int to fraction class
    n = fractions.Fraction(n)
    for step in seq:
        if step == 'L':
            # left transformation
            #n = (3*n - 1) / 2
            n = (3*n + 1) / 2
        if step == 'R':
            # right transformation
            n = n/2
    return n

# calculates the number in the Collatz tree
def NinTree(n):
    # obtain the tree representation of n
    str_tree = int2binaryTree(n)
    # calculate the N for which the transformation str_tree will give 0
    # express the number as a fraction
    x = fractions.Fraction((1 - I_str(0,str_tree)),(I_str(2,str_tree)-I_str(1,str_tree)))
    #x = (1 - I_str(0,str_tree))/(I_str(2,str_tree)-I_str(1,str_tree))
    return x

# Takes an integer n and returns the number of steps(transformations) required to reach 1
def stepsTo1(n):
    steps = 0
    while(not (n == 1)):
        # even number
        if (n % 2 == 0):
            n = n/2
        else: # odd number
            n = 3*n+1
            
        steps += 1

    return steps
    

# calculates the equation of the line for the given n
def lineOfN(n):
    # obtain the tree representation of n
    str_tree = int2binaryTree(n)

    m = I_str(2, str_tree)-I_str(1,str_tree)
    b = I_str(0, str_tree)
    
    out = "y = " + str(m) + "*x + " + str(b)
    return out


# returns the n'th slide number
def slide(n):
    # base case
    if (n==1):
        return 1
    else:
        # recursive case
        return 2**(2*(n-1)) + slide(n-1)

# returns a string that represents the path of transformations needed in order to reach 1
def path(n):
    out = ''
    while(not (n == 1)):
        # even number
        if (n % 2 == 0):
            out += 'R'
            n = n/2
        else: # odd number
            out += 'L'
            n = (3*n+1)/2

    return out

if __name__ == "__main__":
    print("Testing")
    for i in range(20):
        print(int2binaryTree(i+1))


    ints = {}
    for i in range(300):
        print(i+1,"(", int2binaryTree(i+1),")",  " ----> ",NinTree(i+1))
        #if (abs(NinTree(i+1) - round(NinTree(i+1))) < 0.00001):
            #ints[i+1] = NinTree(i+1)

    #print(ints)
    # display the dictionary of ints sorted by value
    #for key, value in sorted(ints.items(), key=lambda x: x[1]):
        #print("%s: %s" % (value, key))
    

    #for i in range (700):
        #print(i+1, " ---> ", lineOfN(i+1))
