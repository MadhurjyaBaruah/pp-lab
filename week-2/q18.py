# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:16:19 2025

@author: USER
"""

text = input("Enter a sentence: ")
letters = "abcdefghijklmnopqrstuvwxyz"

for char in letters:
    if char not in text.lower():
        print("Not a pangram")
        exit()

print("It is a pangram")
