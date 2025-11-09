# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 13:43:07 2023

@author: Hardeep Kaur Gill

Exercise 5.1

Half Integral search method

"""
#import important libraries 
import numpy as np
import matplotlib.pyplot as plt


#precision
prec = 1E-5

#define the function
def f(x):
    return x**4 - 19*(x**3) + 117*(x**2) - 261*x + 162

start, end, step = 0, 10, 0.1

x = start
d = step

while x < end: #outer while loop is to find all roots in a given interval
    d = step  #reset d
    
    while d > prec and x < end:
        if f(x)*f(x+d) <= 0: #if there is a root in the interval then half d
            d = d / 2  
        else:
            x = x + d  #
    
    #to make sure it does not print the x in the end of the interval
    if x < end:  
        print("The root is: ", x)
        plt.plot(x, f(x), 'gx')
        x = x + step

num = 100
xvals = np.linspace(start, end, num)
yvals = f(xvals)

plt.plot(xvals, yvals)

#plot y = 0 to show the roots in the graph
plt.plot(xvals, np.zeros(num))
