# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 14:19:32 2025

@author: USER
"""

a = 70
b = 40


print("Arithmetic Operators:")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)


print("\nComparison Operators:")
print("a == b:", a == b)
print("a != b:", a != b)
print("a > b:", a > b)
print("a < b:", a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)


print("\nLogical Operators:")
print("a > 0 and b > 0:", a > 0 and b > 0)
print("a > 0 or b < 0:", a > 0 or b < 0)
print("not (a > b):", not (a > b))


print("\nBitwise Operators:")
print("a & b:", a & b)
print("a | b:", a | b)
print("a ^ b:", a ^ b)
print("~a:", ~a)
print("a << 1:", a << 1)
print("b >> 1:", b >> 1)


print("\nAssignment Operators:")
c = a
c += b
print("c += b:", c)
c -= b
print("c -= b:", c)
c *= b
print("c *= b:", c)
c /= b
print("c /= b:", c)
