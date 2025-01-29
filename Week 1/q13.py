# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 20:35:42 2025

@author: USER
"""

#Write a Python program to check whether a number is in a given range.

def test_range(n):
    if n in range(3, 9):
        print(f"{n} is in the range")
    else:
        print("The number is outside the given range.")

num = int(input("Enter a number: "))

test_range(num)
