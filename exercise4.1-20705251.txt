# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 09:07:50 2023

@author: Hardeep Kaur Gill

Exercise 4.1

"""

#i know the given algorithm in the notes defines start but after coding i 
#noticed it was not entirely needed for this code. basically start = x.
end, steps = 100, 100

#define the function i am using for this exercise
def f(x):
    return x**2 + x**3


#-----------main code------------------
#define the lower limit
x = 0

#define the step size
h = (end-x)/steps

#calculate the single parameters for the trapezoidal formula
ans = f(x) + f(end)

#calculate the rest of the parameters using the a loop
for n in range(1,steps):
    x = x+h
    
    ans =ans + 2*f(x)

#multiply the results so far by half the step size, as it is stated in the 
#trapezoidal formula: (h/2)*(f0 + 2f1 + 2f2 + 2f3 +... + 2fn-1 + 2fn)
ans = ans*h*(1/2)

#print the result 
print(ans)

