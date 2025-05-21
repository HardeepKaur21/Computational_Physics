# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 15:28:46 2023

@author: Hardeep Kaur Gill

Exercise 6.3 


"""

#import required libraries
import numpy as np
import matplotlib.pyplot as plt

def f(g, l, theta):
    return -(g/l)*np.sin(theta)

#parameters
g = 9.81 #acceleration due to gravity
l = 1 #length of the pendulum 
t_max = 10 #max time
N = 1000
h = 0.01 #step size , 0.001

#initial conditions (Euler's Method)
theta = np.zeros(N)
t_values = np.linspace(0, 10, N)
z = np.zeros(N) #angular velocity dtheta/dt
theta[0] = np.pi / 4
z[0] = 0

#apply Euler's Method
for i in range(1, N):
    z[i] = z[i-1] + f(g, l, theta[i-1])*h
    theta[i] = theta[i-1] + z[i-1]*h
    t_values[i] = t_values[i-1] + h

#initial conditions (Euler-Cromer's Method)
theta_cr = np.zeros(N)
z_cr = np.zeros(N) #angular velocity dtheta/dt
theta_cr[0] = np.pi / 4
z_cr[0] = 0

#apply Euler-Cromer's Method
for i in range(1, N):
    z_cr[i] = z_cr[i-1] + f(g, l, theta_cr[i-1])*h
    theta_cr[i] = theta_cr[i-1] + z_cr[i]*h
    t_values[i] = t_values[i-1] + h

#plot the results
#subplots
fig, ax = plt.subplots(2, 2) 

#Euler's Method
ax[0,0].plot(t_values, theta, label = "Angle, Theta") 
ax[0,0].plot(t_values, z, label = "Angular Velocity, Z") 
ax[0,0].legend()
ax[0,0].set_xlabel("Time, t")
ax[0,0].set_ylabel("Angle, Theta and Angular Velocity, Z")
ax[0,0].set_title("Theta as a function of Time, Euler's Method")


ax[0,1].plot(theta, z) 
ax[0,1].set_xlabel("Angle, Theta")
ax[0,1].set_ylabel("Angular Velocity, Z")
ax[0,1].set_title("Phase Space Diagram, Euler's Method")

#Euler-Cromer's Method
ax[1,0].plot(t_values, theta_cr, label = "Angle, Theta") 
ax[1,0].plot(t_values, z_cr, label = "Angular Velocity, Z") 
ax[1,0].legend()
ax[1,0].set_xlabel("Time, t")
ax[1,0].set_ylabel("Angle, Theta and Angular Velocity, Z")
ax[1,0].set_title("Theta as a function of Time, Euler-Cromer's Method")


ax[1,1].plot(theta_cr, z_cr) 
ax[1,1].set_xlabel("Angle, Theta")
ax[1,1].set_ylabel("Angular Velocity, Z")
ax[1,1].set_title("Phase Space Diagram, Euler-Cromer's Method")
