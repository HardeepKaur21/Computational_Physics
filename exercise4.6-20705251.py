# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 13:30:38 2023

@author: Hardeep Kaur Gill

Exercise 4.6

"""

import scipy as sc

f = lambda x: x**4 - 2*x + 1


value, error =sc.integrate.quadrature(f, 0, 2)
print("Result: ", value)  
print("Error: ", error)
