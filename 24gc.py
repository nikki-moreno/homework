# 24gc.py

# Nikki Moreno
# 4 February 2023
# MCB 185

## Purpose ##
# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'

# assign initial values to g and c to store future values
c = 0
g = 0


# add 1 for every encounter with a G or C in dna 
for position in dna:
	if 	  position == 'G': g = g + 1
	elif  position == 'C': c = c + 1
	gc_pair = c + g 

# print total c and g count, divided by len of dna 
print(f'{gc_pair/len(dna):.2f}')


"""
python3 24gc.py
0.42
"""
