# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 16:25:11 2023

@author: Hardeep Kaur Gill

Exercise 3.5

From this exercise we can see how the cubic spline can be straighter than 
global interpolation plot at intervaals, showing it comes halfway between 
global and linear interpolation.  

"""

#import required libraries
import numpy as np
import matplotlib.pyplot as plt
import scipy as sc

#this is function g(x) from the notes that gives the globally interpolated 
#polynomial xx is x from the formula
# n is the same as the formula
def f(xx, n):
    
    top = 1 #top of the fraction
    bottom = 1 #bottom of the fraction
    interp = 0 #value to be returned
    
    #j keeps track of the subscripts changing on the top of the formula
    #i keeps track of the subscripts changing on the bottom of g(x)
    for i in range(n):
        
        for j in range(n):
            if j != i: #j == i is not part of g(x)
                top *= (xx - x[j]) 
               
        for j in range(n):
            if j != i: #j == i is not part of g(x)
                bottom *= x[i] - x[j]
                
        #calculate the interpolation as per g(x)
        interp += fx[i] * top/bottom
        
        #reset values for next calculation
        top = 1
        bottom = 1
        
    return interp 



x = [ 0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4]
fx = [ 0.5, 2.0, 4.0, 6.0, 4.0, 4.0, 5.2, 0]
tck = sc.interpolate.splrep(x,fx)

num = 100

xr = np.linspace(x[0], x[-1], num) #x[-1] is the last element of x
yr = f(xr, len(x))

xval = np.linspace(x[0], x[-1], num)
yval = sc.interpolate.splev(xval, tck)
    
plt.clf() #clears the graph from previous plots

plt.plot(xval, yval, label = 'cubic spline', linestyle = '--')
plt.plot(xr, yr, label = 'global interpolation', linestyle = '--')

#plot the known points 
plt.plot(x, fx, 'ro')

plt.xlim(x[0], x[-1]) #trims empty space from sides
plt.grid(which = 'major', color = 'k' , linestyle = ":") 


    
plt.legend(loc = 'best')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()


