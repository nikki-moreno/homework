# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys

import sys 


values = sys.argv[1:]
minimum = min(sys.argv[1:])
maximum = max(sys.argv[1:])


print('Count: ', len(sys.argv[1:]))
print('Minimum:', float(minimum))
print('Maximum:', float(maximum))



"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""



# values = sys.argv[1:] 	#didn't work 
# summation = sum(values) 	#didn't work 