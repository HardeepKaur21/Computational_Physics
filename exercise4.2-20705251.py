# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:39:59 2023

@author: Hardeep Kaur Gill

Exercise 4.2

"""
#import libraries
import numpy as np

start, end = 0, np.pi

#define the function i am using for this exercise
def f(x):
    return np.sin(x)

def trapRule(steps):
    
    #define the lower limit
    x = 0
    #calculate the single parameters for the trapezoidal formula
    ans = f(x) + f(end)
    
    #define the step size
    h = (end-x)/steps
    
    #calculate the rest of the parameters using the a loop
    for n in range(1,steps):
        x = x+h
        ans =ans + 2*f(x)
    
    #multiply the results so far by half the step size, as it is stated in the 
    #trapezoidal formula: (h/2)*(f0 + 2f1 + 2f2 + 2f3 +... + 2fn-1 + 2fn)
    ans = ans*h*(1/2)
    return ans


#-----------main code------------------

#Analytical asnwer 
analyt = -np.cos(end)- (-np.cos(start))

#print the result 
print("Trapezoidal formula: ", trapRule(10))
print("Analytical answer: ", analyt)
print()

#errors 
print("Error on 10 steps: " , analyt - trapRule(10))
print("Error on 20 steps: " , analyt - trapRule(20))
print("Error on 100 steps: " , analyt - trapRule(100))
