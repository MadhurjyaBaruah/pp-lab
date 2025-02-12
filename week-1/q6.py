# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 19:40:05 2025

@author: USER
"""

#Write a Python program that takes a list and returns a new list with unique elements of the first list.


user_input = input("Enter numbers separated by space: ")
a = [int(x) for x in user_input.split()]

result = list(set(a))

print("List with unique elements:", result)



#OR

# original_list = list(map(int, input("Enter elements separated by space: ").split()))
# unique_list = list(set(original_list))  # Convert to set and back to list
# print("List with unique elements:", unique_list)

