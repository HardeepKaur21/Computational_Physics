# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 15:40:22 2023

@author: Hardeep Kaur Gill

Exercise 3.4

"""

#import required libraries
import numpy as np
import matplotlib.pyplot as plt
import scipy as sc



x = [ 0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4]
fx = [ 0.5, 2.0, 4.0, 6.0, 4.0, 4.0, 5.2, 0]
tck = sc.interpolate.splrep(x,fx)

num = 100


xval = np.linspace(x[0], x[-1], num)
yval = sc.interpolate.splev(xval, tck)
    
plt.clf() #clears the graph from previous plots

plt.plot(xval, yval, label = 'cubic spline', linestyle = '--')

#plot the known points 
plt.plot(x, fx, 'ro')

plt.xlim(x[0], x[-1]) #trims empty space from sides
plt.grid(which = 'major', color = 'k' , linestyle = ":") 

#plot requested points 
plt.plot(0.3, sc.interpolate.splev(.3, tck), 'gx')
plt.plot(0.5,sc.interpolate.splev(.5, tck), 'gx')
plt.plot(0.9, sc.interpolate.splev(.9, tck), 'gx')
    
plt.legend(loc = 'best')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.show()
