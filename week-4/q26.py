# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 14:19:08 2025

@author: USER
"""

import sys

if len(sys.argv) != 3:
    print("Please provide two numbers as arguments. Example: !python q26.py 5 10")
    sys.exit(1)

num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

print("Sum:", num1 + num2)
