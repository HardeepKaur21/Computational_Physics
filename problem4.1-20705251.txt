# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 12:24:55 2023

@author: Hardeep Kaur Gill

Problem 4.1
Calculate the magnetic field produced by a current in a straight wire

"""

#import libraries
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

def B(x, L, I):
    
    f = lambda  x1, z: x1/(x1**2 + z**2)**1.5
    
    start = -L
    end = L
    μ0 = 4*np.pi * 10E-7
    steps = 100
    #define the step size
    h = (end-start)/steps
    #define small segment z
    z = start
    
    #calculate the single parameters for the trapezoidal formula
    ans = f(start, z) + f(end, z)
        
    #calculate the rest of the parameters using the a loop
    for n in range(1,steps):
        z = z+h
        ans =ans + 2*f(x, z)
    
    #multiply the results so far by half the step size, as it is stated in the 
    #trapezoidal formula: (h/2)*(f0 + 2f1 + 2f2 + 2f3 +... + 2fn-1 + 2fn)
    ans = ans*h*(1/2)
    
    #multiply by the contant outside of the integral of B(x)
    ans = ((μ0*I)/(4*np.pi))*ans
    return ans


#------------------main code------------------
N = 100 #number of buckets for the plot
x = np.linspace(0.1 , 10, N)
y = np.array(B(x, 1, 1))


#zip the 2 arrays together in a table to be shown using tabulate 
table = zip(x, y)
print(tabulate(table, headers=['x', 'B(x)']))

#plot the results
plt.plot(x, y, label = "B(x)")
plt.ylabel("B(x)")
plt.xlabel("x")
plt.legend()
plt.show()
