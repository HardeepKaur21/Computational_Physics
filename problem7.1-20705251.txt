# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 12:06:31 2023

@author: Hardeep Kaur Gill

Problem 7.1 

This does not feel right to me

"""

#import required libraries
import numpy as np
import matplotlib.pyplot as plt

#declare global variables
V0 = 0.5
omega = 2*np.pi

def V(t):
    return np.sin(omega*t)

def fun(L, R, t, I):
    return (1/L) * (V(t) - R*I) 

N = 1000 #total steps
endt = 4

#declare array to store x and y values (RK4)
tRK4 = np.linspace(0, endt, N) #t(0) is 0 that is why randy start from index 1
IRK4 = np.zeros(N) #y

# Set initial conditions (R44)
IRK4[0] = 10

# Set step size same for both
dx = endt/N

#parameters
IRK4[0] = 0.5
L = 1
R =1

#apply Runge-Kutta's Method (RK4) to calculate the 
for i in range(1, N):
    # Calculate partial steps
    k1 = dx * fun(L, R, tRK4[i-1], IRK4[i-1])
    k2 = dx * fun(L, R, tRK4[i-1] , IRK4[i-1] + k1/2)
    k3 = dx * fun(L, R, tRK4[i-1] , IRK4[i-1] + k2/2)
    k4 = dx * fun(L, R, tRK4[i-1] , IRK4[i-1] + k3)
    # Combine partial steps
    IRK4[i] = IRK4[i-1] + k1/6 + k2/3 + k3/3 + k4/6
    
    
# Calculate dI/dt using three-point derivative approximation
dI_dt_values = np.zeros(N)
dI_dt_values[0] = -4.5
for i in range(1, N-1):
    dI_dt_values[i] = (IRK4[i+1] - IRK4[i-1]) / (2*dx)


plt.plot(tRK4, V(tRK4), label = "V(t)") 
plt.plot(tRK4, IRK4, label = "I(t)") 
plt.plot(tRK4, dI_dt_values, label = "dI/dt, using 3pt") 
plt.plot(tRK4, V(tRK4) - R*IRK4, label = "dI/dt, using formula given")
plt.legend()
plt.grid()
plt.xlabel("Time")
plt.ylabel("I(t))")
plt.title("LC Circuit - V(t), I(t), dI/dt")
plt.show()
