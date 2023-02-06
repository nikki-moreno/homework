# 27frame.py

# Nikki Moreno
# 5 February 2023
# MCB 185

## Purpose ##
# Write a program that prints out the position, frame, and letter of the DNA
# Variation: try coding this with a single loop and nested loops
# Note: use 0-based indexing for position and frame (biology uses 1-based)

dna = 'ATGGCCTTT'

frame = 0
for position in range(len(dna)):
	for nucleotides in range(len(dna)):
		nucleotides = dna[position]
		while (True):
			frame = frame + 1
			if frame > 2: break 
	print (position, frame, nucleotides)

"""
python3 27frame.py
0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 C
6 0 T
7 1 T
8 2 T
"""
