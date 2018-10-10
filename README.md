# Collatz Conjecture

This is a famous problem in mathematics. One of the reasons it is so famous is that, although the statement of the problem is very simple, there is currently no solution to this problem.

## Statement of the problem

The problem can be stated as follows:

Take a positive integer n, and apply the following transformation repeatedly:

n -> (3*n +1) , if n is odd
n -> n/2      , if n is even

Let's see some examples for different values of n:

n = 1: 1 -> 4 -> 2 -> 1 -> 4 -> 2 ... (Cycles forever)
n = 3: 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
n = 6: 6 -> 3 -> 10 -> 5 ... (subsequence of n=5)
n = 7: 7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10 -> 5 ... (subsequence of n=5)

For the four examples shown above, we can see that all sequences end in the number 1 and the cycle (4 -> 2 -> 1) repeats forever.
This seems to be the case for all positive integers.
