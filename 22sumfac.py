# 22sumfac.py

# Nikki Moreno
# 4 February 2023
# MCB 185

## Purpose ##
# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# Use the same loop for both calculations
# Note: you may not import math or any other library


# setting variables
n = 5
x = 1
print (n, end=" ")

# for loop computing running sum from 1...n
for i in range(x,n):
	x = x + (i+1)
print(x, end=" ")

# for loop computing factorial of n
n = 5
x = 1 
for i in range(x,n+1):
	x = x * i
print(x, end=" ")


"""
python3 22sumfac.py
5 15 120
"""
