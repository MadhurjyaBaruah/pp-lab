# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:33:17 2025

@author: USER
"""

import random
count = int(input("How many numbers do you want? "))
min_val = int(input("Enter minimum value: "))
max_val = int(input("Enter maximum value: "))
for i in range(count):
    print(random.randint(min_val, max_val), end=" ")
