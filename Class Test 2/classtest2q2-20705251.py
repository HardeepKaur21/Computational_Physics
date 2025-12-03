# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 11:23:19 2023

@author: Hardeep Kaur Gill

Class Test 2 - Question 2


"""

#import required libraries
import numpy as np
import matplotlib.pyplot as plt

def fx(x, y): #prey
    return x - (x*y)/2

def fy(x, y): #predator
    return -(3/4)*y + (1/4)*x*y

#time evolution
N = 10000 #total no of steps
endt = 50
dx = endt / N

#declared required arrays
x = np.zeros(N)
y = np.zeros(N)
t = np.zeros(N)

#initial conditions
x[0] = 3.0 
y[0] = 0.2
t[0] = 0


def RK4(x1, y1, N, dx):
    
    #initial conditions
    x[0] = x1
    y[0] = y1
    t[0] = 0
    
    #apply Runge-Kutta's Method (RK4)
    for i in range(1, N):
        kfx1 = dx * fx(x[i-1], y[i-1])
        kfy1 = dx * fy(x[i-1], y[i-1])
        
        kfx2 = dx * fx(x[i-1] + kfx1/2, y[i-1] + kfy1/2)
        kfy2 = dx * fy(x[i-1] + kfx1/2, y[i-1] + kfy1/2)
        
        kfx3 = dx * fx(x[i-1] + kfx2/2, y[i-1] + kfy2/2)
        kfy3 = dx * fy(x[i-1] + kfx2/2, y[i-1] + kfy2/2)
        
        kfx4 = dx * fx(x[i-1] + kfx3/2, y[i-1] + kfy3/2)
        kfy4 = dx * fy(x[i-1] + kfx3/2, y[i-1] + kfy3/2)
        
        # Combine partial steps
        t[i] = t[i-1] + dx
        x[i] = x[i-1] + kfx1/6 + kfx2/3 + kfx3/3 + kfx4/6
        y[i] = y[i-1] + kfy1/6 + kfy2/3 + kfy3/3 + kfy4/6
    
    return x, y, t
    
RK4(x[0], y[0], N, dx)
#create 2 subplots (2 is rows and 1 is columns)
fig, ax = plt.subplots(1, 2)    
#plot all evaluated functions in first subplot
ax[0].plot(t, x, label = 'prey')
ax[0].plot(t, y, label = 'predator')
ax[0].legend()
ax[0].set_xlabel("time")
ax[0].grid()
ax[0].set_ylabel("predatory/prey population")

#I know the way to plot the code below is not efficient. However, I could not
#come up with a more efficient way to plot this many graphs
#also I do not know why the lines are so thick

i = y[0]

while i < 2:
    RK4(x[0], i, N, dx)
    ax[1].plot(y, x, 'g')
    i += 0.2
    
ax[1].grid()
ax[1].legend()
ax[1].set_xlabel("predator")
ax[1].set_ylabel("prey")
plt.show()

#when the inital conditions are set to x = 3 and y = 2 then the spatial diagram
#of predator vs prey becomes almost circular
