# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:33:27 2023

@author: Hardeep Kaur Gill

Exercise 6.2 

"""

#import required libraries
import numpy as np
import matplotlib.pyplot as plt

def f(y):
    return - y

N = 200 #total steps
h = 20 / N #step size


#declare required arrays for storing x and y values
t = np.zeros(N)
y = np.zeros(N) # y(0) = 0
z = np.zeros(N)

z[0] = 1
t[-1] = 20

#apply Euler's Method
for i in range(1, N):
    z[i] = z[i-1] + f(y[i-1])*h
    y[i] = y[i-1] + z[i-1]*h
    t[i] = t[i-1] + h
    
#plot the results
plt.plot(t, y, label = "Estimation with Euler's Method") #Euler's Method
plt.legend()
plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("ODE Result")
plt.show()
