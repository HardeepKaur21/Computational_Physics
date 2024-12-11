# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
import numpy as np 

x = np.linspace(0, 2, 100)

plt.plot(x, x, label =  'linear')
plt.plot(x, x**2, label = 'quadratic')
plt.plot(x, x**3, label = 'cubic')

plt.xlabel('x values')
plt.ylabel('y values')
plt.title('Simple Plot')

plt.legend()

plt.show()

