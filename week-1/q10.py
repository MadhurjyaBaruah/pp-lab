# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 20:29:38 2025

@author: USER
"""

#Check if a number is a prime number.

num = int(input("Enter a number: "))

if (num > 1):
    for i in range(2, num):
        if num % i == 0:  
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number") 
else:
    print(num, "is not a prime number")  





