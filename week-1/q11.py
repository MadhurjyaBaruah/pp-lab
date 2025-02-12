# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 20:31:34 2025

@author: USER
"""

# Calculate the factorial of a number.

num = int(input("Enter a number: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i  
    
print("Factorial of", num, "is", factorial)

