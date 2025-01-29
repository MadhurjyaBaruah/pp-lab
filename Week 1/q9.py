# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 19:56:49 2025

@author: USER
"""
#Reverse a given string.

text = input("Enter a string to reverse: ")
reverse = ""
for char in text:
    reverse = char + reverse
print("Reversed string is:", reverse)



#OR

#text = input("Enter a string to reverse: ")  
#reverse = text[::-1]  
#print("Reversed string is:", reverse)
