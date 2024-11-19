# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 11:25:29 2023

@author: Hardeep Kaur Gill

Problem 1.1 

"""
#import required libraries
import matplotlib.pyplot as plt
import numpy as np

#ask for user inputs
vInitial = int(input("Enter initial velocity: "))
launchAngle = float(input("Enter launch angle: "))
timeInterval = int(input("Enter time interval: "))

#make needed libriaries 
t = np.linspace(0, timeInterval, num=1000)
x = np.zeros(1000)
y = np.zeros(1000)
g = 9.81
launchAngle = launchAngle*np.pi/180

#fill the needed arrays that will be plotted
for i in range(1000):
    #the equations used are x = x0+vtcos(θ)
    x[i] = vInitial* t[i]*np.cos(launchAngle)
    #y = y0 + vtsin(θ)- (1/2)gt**2
    y[i] = vInitial* t[i]*np.sin(launchAngle) - (1/2)*g*(t[i]**2)

#someprint statements to check the data
print("t:", t)
print("x:", x)
print("y:", y)

#plot the graph
plt.plot(x, y, label = f"Vel:{vInitial} Ang: {launchAngle: .2f}")
plt.legend()
plt.title("Projectile Simulation")
plt.xlabel("Horizontal Position")

plt.ylabel("Vertical Position")
plt.grid(True) 
plt.ylim(bottom = 0)
plt.xlim(left = 0)

plt.show()

