# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 11:38:42 2023

@author: Hardeep Kaur Gill

Exercise 6.1 


"""
#import required libraries
import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x + y

N = 100 #total steps
h = 1 / N #step size

#declare array to store x and y values
x = np.zeros(N)
y = np.zeros(N)

y[0] = 1 #given from initial condition

#apply Euler's Method
for i in range(1, N):
    x[i] = x[i-1] + h
    y[i] = y[i-1] + h*f(x[i-1], y[i-1])

#calculae analytical solution
xAnalyticalValues = np.linspace(0, 1, N)

#this is the analytical function, solution of the differential equation
yAnalytical = lambda xA: 2*np.exp(xA) - xA - 1

#apply function to all x values
yAnalyticalValues = yAnalytical(xAnalyticalValues)

#plot the results
plt.plot(x, y, label = "Estimation with Euler's Method") #Euler's Method
plt.plot(xAnalyticalValues, yAnalyticalValues, label = "Analytical Estimation") #Analytical Solution
plt.legend()
plt.xlabel("X")
plt.ylabel("y(X)")
plt.title("ODE Result")
plt.show()

