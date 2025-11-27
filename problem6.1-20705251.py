# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 17:08:18 2023

@author: Hardeep Kaur Gill

Problem 6.1 


"""
import numpy as np
import matplotlib.pyplot as plt

def f(g, l, theta, b, m , z):
    #- (b/m)*z is the extra term for damping pendulum
    return -(g/l)*np.sin(theta) - (b/m)*z

#parameters
g = 9.81 #acceleration due to gravity
l = 1 #length of the pendulum 
t_max = 10 #max time
N = 1000
h = 0.01 #step size , 0.001
b = 0.1  #damping coefficient 

#initial conditions (Euler-Cromer's Method)
t_values = np.linspace(0, 10, N)
theta_cr = np.zeros(N)
z_cr = np.zeros(N) #angular velocity dtheta/dt
theta_cr[0] = np.pi / 4
z_cr[0] = 7
m = 1

#apply Euler-Cromer's Method
for i in range(1, N):
    z_cr[i] = z_cr[i-1] + f(g, l, theta_cr[i-1], b, m, z_cr[i-1])*h
    theta_cr[i] = theta_cr[i-1] + z_cr[i]*h
    t_values[i] = t_values[i-1] + h
    
    
#plot the results
#subplots
fig, ax = plt.subplots(2, 1) 

#Euler-Cromer's Method
ax[0].plot(t_values, theta_cr, label = "Angle, Theta") 
ax[0].plot(t_values, z_cr, label = "Angular Velocity, Z") 
ax[0].legend()
ax[0].set_xlabel("Time, t")
ax[0].set_ylabel("Angle, Theta and Angular Velocity, Z")
ax[0].set_title("Theta as a function of Time, Euler-Cromer's Method")


ax[1].plot(theta_cr, z_cr) 
ax[1].set_xlabel("Angle, Theta")
ax[1].set_ylabel("Angular Velocity, Z")
ax[1].set_title("Phase Space Diagram, Euler-Cromer's Method")
