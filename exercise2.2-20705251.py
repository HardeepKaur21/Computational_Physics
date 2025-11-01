# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 11:50:43 2023

@author: Hardeep Kaur Gill

Exercise 2.2


"""
#import libraries
import numpy as np

#define the f(x) = sin(x) function
def f(x):
    return np.sin(x)

#declare variables
x = np.pi/4 
h = 0.01

#print results
print((f(x+h) - f(x-h))/(2*h))
