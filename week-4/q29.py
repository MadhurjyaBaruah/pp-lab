# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 14:20:06 2025

@author: USER
"""

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
