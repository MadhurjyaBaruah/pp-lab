# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 20:38:00 2025

@author: USER
"""

#Calculate the number of upper case letters and lower case letters in a string

#Method 1: Using the built-in methods
Str = input("Enter a string: ")

lower=0
upper=0
for i in Str:
	if(i.islower()):
			lower+=1
	else:
			upper+=1
print("The number of lowercase characters is:",lower)
print("The number of uppercase characters is:",upper)



# Method 2: Using the ascii values, Naive Method
# Python3 program to count upper and
# lower case characters without using
# inbuilt functions

# def upperlower(string):

# 	upper = 0
# 	lower = 0

# 	for i in range(len(string)):
# 		
# 		# For lower letters
# 		if (ord(string[i]) >= 97 and
# 			ord(string[i]) <= 122):
# 			lower += 1

# 		# For upper letters
# 		elif (ord(string[i]) >= 65 and
# 			ord(string[i]) <= 90):
# 			upper += 1

# 	print('Lower case characters = %s' %lower,
# 		'Upper case characters = %s' %upper)

# # Driver Code
# string = 'GeeksforGeeks is a portal for Geeks'
# upperlower(string)



#Method 3: Calculating the characters within the given range of ascii code

# s = "The Geek King"
# l,u = 0,0
# for i in s:
# 	if (i>='a'and i<='z'):
# 		
# 		# counting lower case
# 		l=l+1			
# 	if (i>='A'and i<='Z'):
# 		
# 		#counting upper case
# 		u=u+1
# 		
# print('Lower case characters: ',l)
# print('Upper case characters: ',u)



#Method 4: Using ‘in’ keyword
# Python3 program to count upper and
# lower case characters without using
# inbuilt functions
# string = 'GeeksforGeeks is a portal for Geeks'
# upper = 0
# lower = 0
# up="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# lo="abcdefghijklmnopqrstuvwxyz"
# for i in string:
# 	if i in up:
# 		upper+=1
# 	elif i in lo:
# 		lower+=1
# print('Lower case characters = %s' %lower)
# print('Upper case characters = %s' %upper)



#Method #5 : Using operator.countOf() method
# import operator as op
# Str = "GeeksForGeeks"
# lower = "abcdefghijklmnopqrstuvwxyz"
# l = 0
# u = 0
# for i in Str:
# 	if op.countOf(lower, i) > 0:
# 		l += 1
# 	else:
# 		u += 1
# print("The number of lowercase characters is:", l)
# print("The number of uppercase characters is:", u)

