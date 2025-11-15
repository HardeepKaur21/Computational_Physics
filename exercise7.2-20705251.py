# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 15:30:27 2023

@author: Hardeep Kaur Gill

Exercise 7.2


"""

#import required libraries
import numpy as np
import matplotlib.pyplot as plt

def f(z):      #f = dy/dx = z
    return z

def h(g, k, m, y):   #g = dz/dx = g - (k/m)*y
    return g - (k/m) * y

endt=10
N = 500 #total steps
#declare array to store x and y values (RK4)
xRK4 = np.linspace(0, endt, N) #t
yRK4 = np.zeros(N) #y
zRK4 = np.zeros(N) #z

# Set initial conditions (R42)
xRK4[0] = 0
yRK4[0] = 2
zRK4[0] = 10

# Set step size same for both
dx = endt/N

#parameters
g = 9.81
k = 2
m = 1

#apply Runge-Kutta's Method (RK4)
for i in range(1, N):
    # Calculate partial steps
    kf1 = dx * f(zRK4[i-1])
    kh1 = dx * h(g, k, m, yRK4[i-1])
    
    kf2 = dx * f(zRK4[i-1] + kh1/2)
    kh2 = dx * h(g, k, m, yRK4[i-1] + kf1/2)
    
    kf3 = dx * f(zRK4[i-1] + kh2/2)
    kh3 = dx * h(g, k, m, yRK4[i-1] + kf2/2)
    
    kf4 = dx * f(zRK4[i-1] + kh3)
    kh4 = dx * h(g, k, m, yRK4[i-1] + kf3)
    
    # Combine partial steps
    yRK4[i] = yRK4[i-1] + kf1/6 + kf2/3 + kf3/3 + kf4/6
    zRK4[i] = zRK4[i-1] + kh1/6 + kh2/3 + kh3/3 + kh4/6
    

#plot the results    
plt.plot(xRK4, yRK4, label = "Runge-Kutta 4th Order Method") 
plt.grid()
plt.xlabel("X")
plt.ylabel("y(X)")
plt.title("ODE Result")
plt.show()
