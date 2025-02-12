# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:10:25 2025

@author: USER
"""

def palindrome():
    word = input("Enter a word: ")
    if word == word[::-1]:
        print(word, "is a palindrome")
    else:
        print(word, "is not a palindrome")

palindrome()
