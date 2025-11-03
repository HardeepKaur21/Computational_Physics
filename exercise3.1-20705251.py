# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 10:47:05 2023

@author: Hardeep Kaur Gill


Exercise 3.1

I am sorry Creidhe I saw the solution first without realising it. I made the
best effort the understand it and do a good job in the other exercises. :) 

"""
#import required libraries
import numpy as np
import matplotlib.pyplot as plt

#input from table
x = [0, 0.2, 0.4, 0.6, 0.8]
fx = [0.5, 2, 4, 6, 4]

#this is function g(x) from the notes that gives the globally interpolated 
#polynomial xx is x from the formula
# n is the same as the formula
def f(xx, n):
    
    top = 1 #top of the fraction
    bottom = 1 #bottom of the fraction
    interp = 0 #value to be returned
    
    #j keeps track of the subscripts changing on the top of the formula
    #i keeps track of the subscripts changing on the bottom of g(x)
    for i in range(n):
        
        for j in range(n):
            if j != i: #j == i is not part of g(x)
                top *= (xx - x[j]) 
               
        for j in range(n):
            if j != i: #j == i is not part of g(x)
                bottom *= x[i] - x[j]
                
        #calculate the interpolation as per g(x)
        interp += fx[i] * top/bottom
        
        #reset values for next calculation
        top = 1
        bottom = 1
        
    #return interp
    return interp 

 
order = 5  #number of ints in array x above
num = 50  #number of spaces between 2 numbers in linspace
    
print(f(0, order))      #user points to plot, some examples
print(f(.1, order))
print(f(.2, order))
    
xr = np.linspace(x[0], x[-1], num) #x[-1] is the last element of x
yr = f(xr, order) #f(xx, n) is set as g(x) from the notes so extra points in
#the funcion can be determined and thus a trendline that goes through all 
#points is determined

plt.clf() #clears the graph from previous plots
#plot new graph f(xx, n)
#plt.plot(xr, yr, label = 'global interpolation', linestyle = '--')

#plot the known points 
plt.plot(x, fx, 'ro')
#axes = plt.gca() would also work
#axes.selt_xlim(x[0], x[-1])
    
plt.xlim(x[0], x[-1]) #trims empty space from sides
plt.grid(which = 'major', color = 'k' , linestyle = ":") 
    
plt.plot(0.3, f(.3, order), 'gx')
plt.plot(0.5, f(.5, order), 'gx')
plt.plot(0.75, f(.75, order), 'gx')
    
plt.legend(loc = 'best')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()
    
    
    
