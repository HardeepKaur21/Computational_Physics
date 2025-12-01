# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 10:18:10 2023

@author: Hardeep Kaur Gill

EP408 - Project: File 2

Animation of Figure 6


"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


#k is the magnitude of the uniform force
k = 0.03 #[N]
step = 0.01

#declare arrays 
N = 1950
t = np.zeros(N)  #time
r1 = np.zeros(N) #x posiiton
r2 = np.zeros(N) #y position
v1 = np.zeros(N) #velocity along x axis 
v2 = np.zeros(N) # velocity along y axis

#initial conditions
t[0] = 0
r1[0] = 1
r2[0] = 0
v1[0] = 0
v2[0] = 1

for i in range(1,N):
    r1[i] = r1[i-1] + v1[i-1]*step
    
    r2[i] = r2[i-1] + v2[i-1]*step
    
    r = np.sqrt(r1[i-1]**2 + r2[i-1]**2)
    
    v1[i] = v1[i-1] + (k - (r1[i]/r**3))*step
    
    v2[i] = v2[i-1] - (r2[i]/r**3)  *step
    
    t[i] = t[i-1] + step
    

#plotting
fig, ax = plt.subplots()
orbit, = ax.plot([], [], 'b-', label='Orbit')
ax.set_xlim(-2, 2)  # Adjust the limits based on your data range
ax.set_ylim(-2, 2)  # Adjust the limits based on your data range
ax.set_xlabel('X Position [m]')
ax.set_ylabel('Y Position [m]')
ax.set_title('Orbit Simulation')
ax.legend()

def update(frame):
    print("hi")
    orbit.set_data(r1[:frame*2], r2[:frame*2])
    return orbit,

animation = FuncAnimation(fig, update, frames=N//2, interval=50, repeat=True)
animation.save('orbita.gif', writer='imagemagick', fps=10)
plt.show()
