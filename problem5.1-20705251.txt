# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 13:39:13 2023

@author: Hardeep Kaur Gill

Problem 5.1


"""
#import required libraries
import numpy as np 

#define the function
def f(x, T):
    return x - np.tanh((4*x) / T)

#number of iterations 
n = 10

#starting guesses for secant method
x1 = 50
x2 = 50.1

#number of temperatures
N = 100

#declare an array for temperatures
T = np.linspace(1, 100, N)
for j in range(N):
    #for each guess loop through the iterations
    for i in range(n):
        #apply the newton method formula for each guess
        x1 = x1 - (f(x1, T[j])*(x2 - x1)) / (f(x2, T[j]) - f(x1, T[j]))
        x2 = x1 + 0.1
    

    #at the end of the iterations, print the root
    print("At temperature", int(T[j]), f" K the magnetisation is {x1} T")
    
    x1 = 50 
    x2 = 50.1