# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 14:49:17 2023

@author: Hardeep Kaur Gill

Exercise 1.6

"""
#import required libraries 
import numpy as np
import matplotlib.pyplot as plt

#define a function for sin(x)
def sin(x):
    return np.sin(x)


#create the values to be plotted on the graph
x = np.linspace(0, 2*np.pi, 100)
y = np.zeros(100)

#populate the array with the y values, using the user defined function
for i in range(99):
    y[i] =  sin(x[i])

#plot the graph 
plt.plot(x, y, 'g--', label = 'sin(x)')
plt.legend()
plt.xlabel("X")
plt.ylabel("f(x)")
plt.grid(True) 


plt.show()


    

