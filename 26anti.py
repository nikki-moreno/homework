# 26anti.py

# Nikki Moreno
# 5 February 2023
# MCB 185

## Purpose ##
# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional
# Variation: try this with the range() function and slice syntax

dna = 'ACTGAAAAAAAAAAA'

for position in dna[::-1]:					 # for positions in the reverse of dna
	if   position == 'A': print('T', end="") # print A where where is a T
	elif position == 'T': print('A', end="") # print T where there is an A
	elif position == 'C': print('G', end="") # so on and so forth
	else:		          print('C', end="")

"""

# I wanted to do this this way but am not sure how to proceed
for position in range(len(dna)):
	codon = dna[position:position+3]
	if codon == 'ACT':
			print(dna[::-1])
# my following step would be to translate A --> T and so forth
# I guess I could have just added lines 11 - 14 to the end of this block?
# I think there are more changes I'd have to make.  


"""

"""
python3 26anti.py
TTTTTTTTTTTCAGT
"""
