# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 14:33:38 2023

@author: hkgill
"""
#import required libraries
import numpy as np
import matplotlib.pyplot as plt


def fun(x,y):
    return x + y


N = 1000 #total steps

#declare array to store x and y values (RK2)
xRK2 = np.linspace(0, 1, N)
yRK2 = np.zeros(N)

# Set initial conditions (RK2)
xRK2[0] = 0
yRK2[0] = 1

#declare array to store x and y values (RK4)
xRK4 = np.linspace(0, 1, N)
yRK4 = np.zeros(N)

# Set initial conditions (R42)
xRK4[0] = 0
yRK4[0] = 1

# Set step size same for both
dx = 0.001

#apply Runge-Kutta's Method (RK2)
for i in range(1, N):
    # Calculate partial steps.
    k1 = dx * fun(xRK2[i-1], yRK2[i-1])
    k2 = dx * fun(xRK2[i-1] + dx/2, yRK2[i-1] + k1/2)
    # Combine partial steps.
    yRK2[i] = yRK2[i-1] + k2
    
#apply Runge-Kutta's Method (RK4)
for i in range(1, N):
    # Calculate partial steps.
    k1 = dx * fun(xRK4[i-1], yRK4[i-1])
    k2 = dx * fun(xRK4[i-1] + dx/2, yRK4[i-1] + k1/2)
    k3 = dx * fun(xRK4[i-1] + dx/2, yRK4[i-1] + k2/2)
    k4 = dx * fun(xRK4[i-1] + dx, yRK4[i-1] + k3)
    # Combine partial steps.
    yRK4[i] = yRK4[i-1] + k1/6 + k2/3 + k3/3 + k4/6
    
#calculate analytical solution
xAnalyticalValues = np.linspace(0, 1, N)

#this is the analytical function, solution of the differential equation
yAnalytical = lambda xA: 2*np.exp(xA) - xA - 1

#apply function to all x values
yAnalyticalValues = yAnalytical(xAnalyticalValues)
    

#plot the results
plt.plot(xRK2, yRK2, label = "Runge-Kutta 2nd Order Method") 
plt.plot(xRK4, yRK4, label = "Runge-Kutta 4th Order Method") 
plt.plot(xAnalyticalValues, yAnalyticalValues, label = "Analytical Estimation") #Analytical Solution
plt.legend()
plt.grid()
plt.xlabel("X")
plt.ylabel("y(X)")
plt.title("ODE Result")
plt.show()
