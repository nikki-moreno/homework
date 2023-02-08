# 30stats.py

# Nikki Moreno
# 8 February 2023
# MCB 185

## Purpose ##
# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# Hint: use sys.argv to get the values from the command line
# Note: you are not allowed to import any library except sys






# Imports, variables and initials
import sys 	
minimum = min(sys.argv[1:])
maximum = max(sys.argv[1:])


# Count, Minimum, Maximum
print('Count: ', len(sys.argv[1:]))
print('Minimum:', float(minimum))
print('Maximum:', float(maximum))

# Sum, Std. Dev, Median
values = list(sys.argv[1:])
print(sum(int(values)))





### Notes ###
# mean = sum of (sys.argv[1:]) divide by # of positions... len(sys.argv[1:])
# std. dev 
# - numerator = [(i - mean)**2 + ((i + 1) - mean)**2 + .... ((i + n) - mean)**2]
# 	- maybe use data.append() ???
# - denominator = range(len(sys.argv[1:])
# - numerator / denominator 	
# median 
# 		- sorting sys.argv([1:]) from least to greatest = 1, 1, 3, 4, 5
#		- HOW DO I PICK THE MIDDLE??? 




# Trying to use sum but it won't with strings 
# values = sys.argv[1:] 	#didn't work 
# summation = sum(values) 	#didn't work 



"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""