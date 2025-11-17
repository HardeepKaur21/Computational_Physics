# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 16:23:02 2023

@author: Hardeep Kaur Gill

Exercise 8.2

NOT DONE YET!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""
#import required libraries
import random as r
import numpy as np
import matplotlib.pyplot as plt

decLambda = 0.01
#number of nuclei at the start
N0 = 1000  #change this tp 10, 100, 100
N = N0   #number of nuclei that change over time
t = 500 # 50 can be chosen as well, but the curve is shown when t = 500

#arrays to be plotted
time = np.linspace(0, t, t)
n = []
ran = np.zeros(N0)


count = 0
for i in range(t):
    for j in range(N):
        ran[j] = r.random()
        #print(ran)
    for j in range(N):
        if ran[j] < decLambda:
            #print(ran[j])
            count += 1
    N =  N - count
    count = 0
    n.append(N)

#different variables are used for the analytical calculations to avoid 
#confusion
n0Analytical = 1000
nAnalytical = np.linspace(0, t, t)
nAnalytical[0] = n0Analytical
lmbda = 0.01

for i in range(1, t):
    nAnalytical[i] = n0Analytical*np.exp(-lmbda*time[i])

plt.plot(time, n)
plt.plot(time, nAnalytical)
plt.xlabel("time")
plt.ylabel("number of nuclei left")
plt.show()
