# 25atseq.py

# Nikki Moreno
# 4 Feburary 2023
# MCB 185

## Purpose ##
# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence
# Note: set random.seed() if you want repeatable random numbers

# import library, establish initial variables and proportion of AT
import random
seq_length = 30
seq = ''
AT_fraction = 0.6000000000000000000000000000000
at = 0

# generting the random sequence and counting letters
for nucleotides in range(seq_length):
	for positions in seq:
		if positions == 'A' or positions == 'T': at = at + 1
	r = random.random()
	if r <= AT_fraction: seq = seq + random.choice('AT')
	else:				seq = seq + random.choice('CG')

print(len(seq), at/len(seq), seq)





"""
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
