# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 14:51:21 2025

@author: USER
"""

#Program to find the biggest among 3 numbers.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if (num1 >= num2 and num1 >= num3):
    largest = num1
elif (num2 >= num1 and num2 >= num3):
    largest = num2
else:
    largest = num3

print(f"The largest number among {num1}, {num2}, and {num3} is: {largest}")