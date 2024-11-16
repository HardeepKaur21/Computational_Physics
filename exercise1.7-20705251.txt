# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 15:17:48 2023

@author: Hardeep Kaur Gill

Exercise 1.7


"""

import numpy as np
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5, 5.5]
y = [7, 1, 2, 6, 4, 3, 3]

xx = np.array([0, 1, 2, 3, 4, 5, 5.5])      #using arrays rather than lists here
yy = np.array([7, 1, 2, 6, 4, 3, 3])
zz = yy**2  #if these were lists then I's have to square each element
            # in a loop
            
fig, ax = plt.subplots(figsize = (15, 10)) #make the plot big enough to fit
                                            #labels etc
                                            
ax1 = plt.subplot(221)                  #this is the first plot in a 2x2 grid
ax1.plot(x,y)

ax2 = plt.subplot(222)
ax2.plot(xx, yy, label = 'data')            #add a label to use in a legend
plt.legend()

ax3 = plt.subplot(223)
ax3.plot(xx, zz, 'ko--')                  #this is the 3rd plot in a 2x2 grid
                                          #use black (k) circles

ax4 = plt.subplot(224)                      #plt.plot(x, y, 'bo, x, y, 'r--)
ax4.plot(x, y, 'bo', label = 'points')  #plot y vs x, first using blue circles 
ax4.plot(x, y, 'r--', label= 'line')    #and then using a red dashed line
ax4.set_title('My second plot', color='b') #add a title and change colour
ax4.set_xlabel('x-data', fontsize=14, color='g') #add x-label, change fontsize
ax4.set_ylabel('measurements')
ax4.set(xlim= (-1,7), ylim=(0,8)) #set axes by hand to give some space
                                  #around data points
ax4.text(.75,5,'this is some text') #can place text in a plot
ax4.grid(True)                      #put a grid on
ax4.legend(loc='best',fontsize=12)  #place the best place for legend,
                                    #smaller fontsize
plt.tight_layout()                          
plt.show()



