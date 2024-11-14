# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 14:28:33 2023

@author: Hardeep Kaur Gill

Exercise 1.5 


"""
#import required libraries
import numpy as np

#the first array with 100 equal spaces between 0 and 2pi
x = np.linspace(0, 2*np.pi, 100)
print(x)

#the second array that hold the sin value of each element in x
y = np.sin(x)
print(y)

