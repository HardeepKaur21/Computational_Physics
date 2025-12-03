# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 11:03:58 2023

@author: Hardeep Kaur Gill

Class Test 2 - Question 1

"""

#import required libraries
import numpy as np
import matplotlib.pyplot as plt

#parameters
g = 9.81
v = 15
theta = 45 #degrees


#define the vertical posiiton
def f(x):
    return x * np.tan(theta) - (g/2)*(x/(v*np.cos(theta)))**2

#variables of guesses, each will come up with a different root
x1 = 80
x2 = 80.1

N = 100

angle = np.linspace(0, 90, N)

#for each guess loop through the iterations
for i in range(N):
    #apply the newton method formula for each guess
    x1 = x1 - (f(x1)*(x2 - x1)) / ((f(x2) - f(x1)))
    x2 = x1 + 1

#at the end of the iterations, print the root
print("A root for this function using Secant method is", x1)


yVals = f(angle)


#to view where the roots are
zero = np.zeros_like(angle)
plt.plot(angle, f(angle), label = "v = 15 ms^(-1)")

#plot zero array
plt.plot(angle, zero)
plt.ylim(bottom = 0)
plt.ylabel("range [m]")
plt.xlabel("launch angle [degrees]")
plt.show()
