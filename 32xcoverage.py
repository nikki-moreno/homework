# 32xcoverage.py

# Nikki Moreno
# 9 February 2023 - 3 March 2023
# MCB 185

## Purpose ##
# Write a program that simulates a shotgun resequencing project
# How uniformly do the reads "pile up" on a chromosome?
# How much of that depends on sequencing depth?
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Hint: make the problem smaller, so it's easier to visualize and debug
# Hint: if you don't understand the context of the problem, ask for help
# Hint: if you are undersampling the ends, do something about it
# Note: you will not get exactly the same results as the command line below


import sys
import random

# Initialialization 
genom_sz = int(sys.argv[1])		
read_num = int(sys.argv[2])	
read_len = int(sys.argv[3])	
base_count = [0] * genom_sz 

# Making coverage
for i in range(len(base_count) - read_len + 1):	# Length of genome size, minus the window. 
	r = random.randint(0, len(base_count) - read_len) # Read position generator.
	for x in range(r , r + read_len): 			# At that position, across the read length
		base_count[x] = base_count[x] + 1
		print(base_count)



# base_count = r + read_len
# print(base_count)


# Output 
min(None)								# minimum coverage length						
#max(None)								# maximum coverage length
#avg_cvg = read_num/len(genome_sz) 		# average coverage length







# number of reads to generate (4)
# how much do they cover the genome? 
# How do we represent the coverage of what they cover? 
# given throwing stuff on there, how often do we get gaps in the coverage?
# - what is the minimum, maximum and average coverage that we expect from the background? 
# - average: add all the numbers from the reads  len(seq) O_O
# where will I place the reads?
# - for pos in range(len(genome)-readlength + 1)
# initialization, zeros ( think of append with 0s) 
# not a good idea to sample the ends because they will be low in coverage artificially 
#


"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
