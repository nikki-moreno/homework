# 31entropy.py

# Nikki Moreno
# 8 February 2023 & 14 Ferbuary 2023
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


# iteration
vals = []					# Empty list.
for i in sys.argv[1:]:		# For positions in system argument,
	vals.append(float(i)) 	# add the positions past [:1] to the empty list.	
	if sum(vals) == 1:		# Check to see if the list sum = 1
		I = -math.log2(vals[i]) + I		#mathisclose (line 25)
print(vals)



"""
i = 0
i = sys.argv([1:]) 
H = -sum(pi * log(pi))
"""


"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""



## Shanon Entropy ##
# Information Theory - I(m) =  -log2P(m)
# Entropy - sum up all information contents and weight them by how often they occur
# Entropy = 0 when its not random, 100% predictable
# calculate the entropy of a frequency distribution
# for loop = sigma
# (0.1 * log2 0.1) + (0.2*log0.2)
# for p in ps
# H-=pmath.log2p
# for i in range(len(p))
# H += P[i]*log2p[i]