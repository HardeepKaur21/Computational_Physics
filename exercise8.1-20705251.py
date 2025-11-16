# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 14:17:02 2023

@author: Hardeep Kaur Gill

Exercise 8.1

"""
import random
import numpy as np
import matplotlib.pyplot as plt

n = 100000 #number of steps

#declare required arrays
x = np.zeros(n)
y = np.zeros(n)

#use random seed as shown in notes
random.seed(10)

#set start of walk
x[0] = 0


for i in range(1, n):
    #get random numbers as direction of next step 
    x1 = random.uniform(-np.sqrt(2), np.sqrt(2))
    y1 = random.uniform(-np.sqrt(2), np.sqrt(2))
    
    #make it look like a walk
    x[i] = x[i-1] + x1
    y[i] = y[i-1] + y1
    
#plot result and show star and end of the walk
plt.plot(x, y)
plt.plot(x[0], y[0], 'ro', label = "start")
plt.plot(x[-1], y[-1], 'go', label = "end")
plt.legend()
plt.xlabel("x")
plt.ylabel("y")
plt.show()
    

