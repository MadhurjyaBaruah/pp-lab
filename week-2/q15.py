# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:45:51 2025

@author: USER
"""

def multi():
    nums = input("Enter numbers : ")
    numbers = [int(x) for x in nums.split()]
    result = 1
    for x in numbers:
        result = result * x
    print("Result:", result)
multi()
