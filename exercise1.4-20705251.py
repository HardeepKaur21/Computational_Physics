# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 14:18:23 2023

@author: Hardeep Kaur Gill

Exercise 1.4

"""
#define list 
L = [5,7,18,9,0,1,3,7,7,2]

#store the length of the list to use in the foor loop
length = len(L)

#declare variables where the index and the largest number in the list will be
#stored
mega = 0
index = 0


#look for the largest number in the list and store the largest one with its 
#index
for i in range(length):
    if(L[i] > mega):
        mega = L[i]
        index = i
        
#print out the results
print("the largest value is", mega, "item number", index+1, "in the list")
