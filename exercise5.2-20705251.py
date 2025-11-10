# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 11:05:06 2023

@author: Hardeep Kaur Gill

Exercise 5.2

Bisection Method 

"""

#define the function
def f(x):
    return x**4 - 19*(x**3) + 117*(x**2) - 261*x + 162

start, end, steps = 0, 10, 100

#the number of iterations
n = 0


#for each iteration
while n < steps:
    #define the midpoint 
    xm = (start + end)/2
    
    #checking for root in interval
    if f(start)*f(xm) <= 0:
        #set the new end to be the old midpoint as root is in first half
        end = xm
    else:
        #set the new start to be the old start as root is in second half
        start = xm
    #increase the iteration by 1
    n += 1
    
#xm is the root by the end of the loop    
print("The root is", xm)

