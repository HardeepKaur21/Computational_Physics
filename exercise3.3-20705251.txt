# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 14:45:03 2023

@author: Hardeep Kaur Gill

Exercise 3.3

"""

#import required libraries
import numpy as np
import matplotlib.pyplot as plt

#input from table 3.1
x31 = [0, 0.2, 0.4, 0.6, 0.8]
fx31 = [0.5, 2, 4, 6, 4]

#input table from table 3.2
x32 = [0, 1, 2, 2.5, 3]
fx32 = [0, 1, 1, 4, 3]

#this is function g(x) from the notes that gives the interpolated polynomial
#xx is x from the formula
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
                top *= (xx - x31[j]) 
               
        for j in range(n):
            if j != i: #j == i is not part of g(x)
                bottom *= x31[i] - x31[j]
                
        #calculate the interpolation as per g(x)
        interp += fx31[i] * top/bottom
        
        #reset values for next calculation
        top = 1
        bottom = 1
        
    #return interp
    return interp 

#g(x) fpr linear interpolation
def g(xx, x, fx):
    for i in range(1, len(x)):
        if ((xx > x[i-1]) and (xx < x[i])):
            x1 = x[i-1]
            x2 = x[i]
            fx1 = fx[i-1]
            fx2 = fx[i]
        
            return fx1*(xx-x2)/(x1-x2)+fx2*(xx-x1)/(x2-x1)

 
order = 5  #number of ints in array x above
num = 50  #number of spaces between 2 numbers in linspace
    
print(f(0, order))      #user points to plot, some examples
print(f(.1, order))
print(f(.2, order))

print(g(0.5, x32, fx32))      #user points to plot, some examples
print(g(2.25, x32, fx32)) 
print(g(2.75, x32, fx32))
    
xr31 = np.linspace(x31[0], x31[-1], num) #x[-1] is the last element of x
yr31 = f(xr31, order) #f(xx, n) is set as g(x) from the notes so extra points in
#the funcion can be determined and thus a trendline that goes through all 
#points is determined

xr32 = np.linspace(x32[0], x32[-1], num) 
yr32 = np.zeros(num)

#fill yr32 array 
for i in range(num):
    yr32[i] = g(xr32[i], x32, fx32)
    

fig, ax = plt.subplots(2, 1)  
#plt.clf() #clears the graph from previous plots
#plot new graph f(xx, n)
ax[0].plot(xr31, yr31, label = 'global interpolation', linestyle = '--')

#plot the known points 
ax[0].plot(x31, fx31, 'ro')
#axes = plt.gca() would also work
#axes.selt_xlim(x[0], x[-1])
    
ax[0].set_xlim(x31[0], x31[-1]) #trims empty space from sides
ax[0].grid(which = 'major', color = 'k' , linestyle = ":") 
    
ax[0].plot(0.3, f(.3, order), 'gx')
ax[0].plot(0.5, f(.5, order), 'gx')
ax[0].plot(0.75, f(.75, order), 'gx')
    
ax[0].legend(loc = 'best')
ax[0].set_xlabel('x')
ax[0].set_ylabel('f(x)')


ax[1].plot(xr32, yr32, label = 'linear interpolation', linestyle = '--')

#plot the known points 
ax[1].plot(x32, fx32, 'ro')
#axes = plt.gca() would also work
#axes.selt_xlim(x[0], x[-1])
    
ax[1].set_xlim(x32[0], x32[-1]) #trims empty space from sides
#plt.ylim(fx[0], fx[-1]) #trims empty space from sides
ax[1].grid(which = 'major', color = 'k' , linestyle = ":") 
    
ax[1].plot(0.5, g(.5, x32, fx32), 'gx')
ax[1].plot(2.25, g(2.25, x32, fx32), 'gx')
ax[1].plot(2.75, g(2.75, x32, fx32), 'gx')
    
ax[1].legend(loc = 'best')
ax[1].set_xlabel('x')
ax[1].set_ylabel('g(x)')



plt.show()
    
    
    
