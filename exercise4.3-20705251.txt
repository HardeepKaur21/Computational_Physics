# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 13:33:37 2023

@author: Hardeep Kaur Gill

Exercise 4.3

"""

start, end,= 0, 100 

steps = int(input("Enter an even amount of steps: "))


while True:
    if(steps % 2 != 0):
        print("Please enter an even number for the steps!")
        steps = int(input("Enter an EVEN amount of steps here: "))
    else: break


#define the function i am using for this exercise
def f(x):
    return x**2 + x**3

#define the step size
h = (end-start)/steps

ans = f(start) + f(end)
odd, even = 0, 0


x = start - h

for n in range(1, steps, 2):
    x = x + 2*h
    odd = odd + 4*f(x)
    
x = start
for n in range(2, steps - 2, 2):
    x = x + 2*h
    even = even + 2*f(x)
    
ans = odd + even + ans
ans = ans * h *(1/3)

print(ans)
    

