# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 16:56:04 2023

@author: HardeeP Kaur Gill

Exercise 6.4


"""
#import required libraries 
import scipy as sc
import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x + y

N = 100 #total steps
h = 1 / N #step size

#declare array to store x and y values
x = np.linspace(0, 1, N)
y0 = 1 #given from initial condition


y = sc.integrate.odeint(f, y0, x)

#plot the results
plt.plot(x, y, label = "Estimation with Euler's Method") #Euler's Method
plt.legend()
plt.xlabel("X")
plt.ylabel("y(X)")
plt.title("ODE Result using SciPy Function")
plt.show()
