# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 11:54:30 2023

@author: Hardeep Kaur Gill

Hardeep Kaur Gill


Problem 7.2

"""
#import required libraries
import numpy as np
import matplotlib.pyplot as plt

#parameters
sigma = 10
r = 28
b = 8/3

#functions defined
def fx(sigma, x, y):
    return sigma*(y-x)

def fy(r, x, y, z):
    return r*x - y- x*z

def fz(b, x, y, z):
    return x*y - b*z

#time evolution
N = 10000 #total no of steps
endt = 50
dx = endt / N
print(dx)

#declared required arrays
x = np.zeros(N)
y = np.zeros(N)
z = np.zeros(N)
t = np.zeros(N)

#initial conditions
x[0] = 0 #
y[0] = 1
z[0] = 0
t[0] = 0

#call the functions
#apply Runge-Kutta's Method (RK4)
for i in range(1, N):
    # Calculate partial steps
    kfx1 = dx * fx(sigma, x[i-1], y[i-1])
    kfy1 = dx * fy(r, x[i-1], y[i-1], z[i-1])
    kfz1 = dx * fz(b, x[i-1], y[i-1], z[i-1])
    
    kfx2 = dx * fx(sigma, x[i-1] + kfx1/2, y[i-1] + kfy1/2)
    kfy2 = dx * fy(r, x[i-1] + kfx1/2, y[i-1] + kfy1/2, z[i-1] + kfz1/2)
    kfz2 = dx * fz(b, x[i-1] + kfx1/2, y[i-1] + kfy1/2, z[i-1] + kfz1/2)
    
    kfx3 = dx * fx(sigma, x[i-1] + kfx2/2, y[i-1] + kfy2/2)
    kfy3 = dx * fy(r, x[i-1] + kfx2/2, y[i-1] + kfy2/2, z[i-1] + kfz2/2)
    kfz3 = dx * fz(b, x[i-1] + kfx2/2, y[i-1] + kfy2/2, z[i-1] + kfz2/2)
    
    kfx4 = dx * fx(sigma, x[i-1] + kfx3/2, y[i-1] + kfy3/2)
    kfy4 = dx * fy(r, x[i-1] + kfx3/2, y[i-1] + kfy3/2, z[i-1] + kfz3/2)
    kfz4 = dx * fz(b, x[i-1] + kfx3/2, y[i-1] + kfy3/2, z[i-1] + kfz3/2)
    
    # Combine partial steps
    t[i] = t[i-1] + dx
    x[i] = x[i-1] + kfx1/6 + kfx2/3 + kfx3/3 + kfx4/6
    y[i] = y[i-1] + kfy1/6 + kfy2/3 + kfy3/3 + kfy4/6
    z[i] = z[i-1] + kfz1/6 + kfz2/3 + kfz3/3 + kfz4/6

#create 2 subplots (2 is rows and 1 is columns)
fig, ax = plt.subplots(1, 2)    
#plot all evaluated functions in first subplot
ax[0].plot(t, y, label = 'y vs t (RK4)')
ax[0].legend()
ax[0].set_xlabel("t")
ax[0].set_ylabel("y")

#plot errors made by 3point and 5point in 2nd subplot
ax[1].plot(y, z, label = 'z vs y (RK4)')
ax[1].legend()
ax[1].set_xlabel("y")
ax[1].set_ylabel("z")
plt.show()

