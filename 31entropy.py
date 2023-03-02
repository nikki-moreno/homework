# 31entropy.py

# Nikki Moreno
# 8 February 2023 - 2 March 2023
# MCB 185

## Purpose ##
# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# Store the values in a new list
# Note: make sure the command line values contain numbers
# Note: make sure the probabilities sum to 1.0
# Note: import math and use the math.log2()
# Hint: try breaking your program with erroneous input



# Imports
import sys
import math


# Empty list and initial variables 
vals = []				
H = 0

# Make sure probabilities sum to approximately 1.
for i in sys.argv[1:]:		
	vals.append(float(i)) 	
assert(math.isclose(sum(vals), 1.0, abs_tol=0.01))

# Entropy calculation
for x in vals:				
	H = (-x * math.log2(x)) + H
print(f'{H:.3f}')



"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
