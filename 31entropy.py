# 31entropy.py

# Nikki Moreno
# 8 February 2023
# MCB 185

## Purpose ##
# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# Store the values in a new list

# Note: make sure the command line values contain numbers
# Note: make sure the probabilities sum to 1.0
# Note: import math and use the math.log2()

# Hint: try breaking your program with erroneous input


import sys
import math

# sum to 1.0 by storing values in a new list
list = []

i = 0
i = sys.argv([1:]) 
H = -sum(pi * log(pi))










"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
