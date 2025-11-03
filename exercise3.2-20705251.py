# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 12:03:24 2023

@author: Hardeep Kaur Gill

Exercise 3.2

"""

#import required libraries
import numpy as np
import matplotlib.pyplot as plt

x = [0, 1, 2, 2.5, 3]
fx = [0, 1, 1, 4, 3]



def g(xx, x, fx):
    for i in range(1, len(x)):
        if ((xx > x[i-1]) and (xx < x[i])):
            x1 = x[i-1]
            x2 = x[i]
            fx1 = fx[i-1]
            fx2 = fx[i]
        
            return fx1*(xx-x2)/(x1-x2)+fx2*(xx-x1)/(x2-x1)


num = 50  #number of spaces between 2 numbers in linspace
    
print(g(0.5, x, fx))      #user points to plot, some examples
print(g(2.25, x, fx)) 
print(g(2.75, x, fx))
    
xr = np.linspace(x[0], x[-1], num) #x[-1] is the last element of x
yr = np.zeros(num) #f(xx, n) is set as g(x) from the notes so extra points in
#the funcion can be determined and thus a trendline that goes through all 
#points is determined

for i in range(num):
    yr[i] = g(xr[i], x, fx)

plt.clf() #clears the graph from previous plots
#plot new graph f(xx, n)
#plt.plot(xr, yr, label = 'linear interpolation', linestyle = '--')

#plot the known points 
plt.plot(x, fx, 'ro')
#axes = plt.gca() would also work
#axes.selt_xlim(x[0], x[-1])
    
plt.xlim(x[0], x[-1]) #trims empty space from sides
#plt.ylim(fx[0], fx[-1]) #trims empty space from sides
plt.grid(which = 'major', color = 'k' , linestyle = ":") 
    
plt.plot(0.5, g(.5, x, fx), 'gx')
plt.plot(2.25, g(2.25, x, fx), 'gx')
plt.plot(2.75, g(2.75, x, fx), 'gx')
    
plt.legend(loc = 'best')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.show()
