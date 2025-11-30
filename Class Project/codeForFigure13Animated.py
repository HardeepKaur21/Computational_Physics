# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 22:23:42 2023

@author: 20705251
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 21:38:39 2023

@author: 20705251
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Constants
K = 0.03 # Solar wind strength, you need to define this
D = 1/32 # Time step size
N = 30000 # Number of iterations, adjust as needed

#initial conditions
r1 = 1
r2 = 0
v1 = 0
v2 = 1
t = 0

#lists to store position data for plotting
r1_list = [r1]
r2_list = [r2]


v1_list = [v1]
v2_list = [v2]


#initial velocity half-step
r8 = r1**2 + r2**2
r = np.sqrt(r8)
r9 = r * r8
d1 = r8 * D
v1 = v1 + (K - r1/r9) * d1/2
v2 = v2 - r2/r9 * d1/2

#iterative loop
for i in range(1, N):
    #half-step estimate of r1, r2
    r5 = r1 + v1 * d1/2
    r6 = r2 + v2 * d1/2
    r8 = r5**2 + r6**2
    
    #full-step calculation of r1, r2
    d1 = r8 * D
    r1 = r1 + v1 * d1
    r2 = r2 + v2 * d1
    
    #store the new positions for plotting
    r1_list.append(r1)
    r2_list.append(r2)
    
    #full-step calculation of v1, v2
    r8 = r1**2 + r2**2
    r = np.sqrt(r8)
    v1 = v1 + (K * r8 - r1/r) * D
    v2 = v2 - r2/r * D
    
    v1_list.append(v1)
    v2_list.append(v2)
    
    t = t + D

fig, ax = plt.subplots(1, 2)

ax[0].plot(r1_list, r2_list)

def update_plot(frame):
    print(frame)
    ax[1].clear()
    ax[1].plot(r1_list[:frame], r2_list[:frame])
    ax[1].set_xlabel('r1')
    ax[1].set_ylabel('r2')
    ax[1].set_title('Orbital Path (r1 vs r2)')
    ax[1].grid()


plt.xlim(-20, 20)
plt.ylim(-20, 20)

animation = FuncAnimation(fig, update_plot, frames=len(r1_list), interval=100)

plt.xlim(-20, 20)
plt.ylim(-20, 20)

#save it
#animation.save('orbital_path_animation.gif', writer=PillowWriter(fps=15))

# Show the animation
plt.show()

