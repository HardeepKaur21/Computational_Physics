# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 11:24:35 2023

@author: Hardeep Kaur Gill

Exercise 4.5


"""

#import libraries
#import numpy as np
import math as m

#define the function i am using for this exercise
def f(x):
    return m.exp(x)

def g(x):
    return (x**3)/(m.exp(x)-1)


#num stands for the function used out of 2 in traprule
def trapRule(start, end, steps, num):
    x= 0
    
    #define the step size
    h = (end-start)/steps
    
    if(num == 1):
        #calculate the single parameters for the trapezoidal formula
        ans = f(start) + f(end)
        
        #calculate the rest of the parameters using the a loop
        for n in range(1,steps):
            x = x+h
            ans =ans + 2*f(x)
    else:
        #do the same for the other function
        ans = g(start) + g(end)
        
        for n in range(1,steps):
            x = x+h
            ans =ans + 2*g(x)
    
    #multiply the results so far by half the step size, as it is stated in the 
    #trapezoidal formula: (h/2)*(f0 + 2f1 + 2f2 + 2f3 +... + 2fn-1 + 2fn)
    ans = ans*h*(1/2)
    return ans


#----------------main code--------------------

#call trapRule and print the answer
print("f(x) = e^x: ", trapRule(0, 1, 100, 1))
print("g(x) = (x**3)/(e^x-1): ", trapRule(0.1, 10, 100, 2))

