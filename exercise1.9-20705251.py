# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 12:29:39 2023

@author: Hardeep Kaur Gill

Exercise 1.9

"""

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import cm


xx, yy, = np.mgrid[-2:2:81j, -3:3:91j]               #the j makes the endpoints
zz = np.exp(-2*xx**2-yy**2)*np.cos(2*xx)*np.cos(3*yy)#inclusive and the number 
                                                     #of points is specified 
                                                     #rather than stepsize 

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

c = ax.plot_surface(xx, yy, zz, cmap= cm.jet, edgecolor = 'black', 
                    linewidth = 0.3, alpha = .8)

ax.contour(xx, yy, zz, zdir = 'x', offset= -3.0, colors = 'black')
ax.contour(xx, yy, zz, zdir = 'y', offset= 4.0, colors = 'blue')
ax.contour(xx, yy, zz, zdir = 'z', offset = -2.0, cmap = cm.jet) #colormap


ax.set_xlim3d(-3.0,2.0)
ax.set_ylim3d(-3.0, 4.0)
ax.set_zlim3d(-2.0,1.0)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.colorbar(c, orientation = 'vertical')
plt.tight_layout()
ax.set_title('surface plot with contours', weight = 'bold', size= 18)
