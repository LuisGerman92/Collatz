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

## Finding the sequence for any number with Python

Writing a program to generate the collatz numbers of a given integer n is an easy exercise. The program [Collatz_1.py](https://github.com/LuisGerman92/Collatz/blob/master/collatz_1.py) takes an integer from the command line, prints all the integers generated by applying the transformation until it reaches one, and also reports the number of integers that are required to reach one.

Running the program with the number 7 as input produces the following output:


```console
luis@Lap:~/Collatz$ ./collatz_1.py 7
Displaying the Collatz numbers for n= 7
22
11
34
17
52
26
13
40
20
10
5
16
8
4
2
1
7 has  16  integers.
```

## Approaches to finding a solution

The question that we want to answer is: 

**Do all integer numbers eventually reach 1?**

When we want to find the solution to a problem, usually the process is to view the problem from different angles, searching for a pattern, or some sort of structure in the data. Maybe we can find a pattern if we write the numbers in binary form, or maybe we could come with a formula for the number of steps required for a number n to reach 1.

### Plotting the steps required to reach 1

We can take the code from [Collatz_1.py](https://github.com/LuisGerman92/Collatz/blob/master/collatz_1.py) and write a function that takes a number n and returns the number of steps required to reach 1:

```python
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
```
Then, we simply make a script that calls this function for different values of n, and writes them to a file.
The script plotSteps.py takes an integer from the command line and outputs the results to the file "steps_data.txt".
Then this data can be plotted with the following gnuplot script:
```
#!/usr/bin/gnuplot

reset

# png
set terminal pngcairo size 800,600 enhanced font 'Verdana,10'
set output 'Collatz_steps.png'

# color definitions
#set border linewidth 1.5
set style line 1 lc rgb '#0060ad' pt 5 ps 0.5 lt 1 lw 1 # --- blue

set xrange [0:10000]
set yrange [0:261]

plot 'steps_data.txt' using 1:2 pt 7 ps 0.1
```

We can now plot the steps required to reach 1 for the first 10,000 integers:
[Collatz_10000]: https://github.com/LuisGerman92/Collatz/blob/master/Collatz_steps_10000.png
