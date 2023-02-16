# 40aacomp.py

# Nikki Moreno
# MCB 185
# 16 February 2023

## Purpose ##
# Make a program that reports the amino acid composition in a file of proteins
# Note: you are not allowed to import any libraries except gzip and sys
# Hint: gzip.open(sys.argv[1], 'rt')
# Variation: use 20 named variables
# Variation: use a list


import sys
import gzip
'''
with gzip.open(sys.argv[1]), 'rt' as fp:
	for line in fp.readlines():
		words = line.split()		# prints just the name
		id = words[0]			 
		print(id[1:], end='')



		words = line.split():		# same as id 
		print(words[0][1:])
'''
'''

## Strat 1##
# write it first with all the variables 
total = 0
A = 0
C = 0
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp.readlines():
		line = line.rstrip()				# remove all white space; can remove Cs or anything
		if not line.startswith('>'):
			total += len(line)
			A == line.count('A')
			C == line.count('C')
print(A,C, A/total, C/total)
'''

# Strat 3 #
# ca make a list of 20 aa, A = index 0; can interate through the numbers to get through pieces
# for i in range ( this), that's the corresponding letter? 

total = 0
aas = 'ACDEFGHIKLMNOPQRSTUVWY'
caa = [0] * len(aas) 
with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp.readlines():
		line = line.rstrip()				# remove all white space; can remove Cs or anything
		if line.startswith('>'): continue	# preprocessing ( better visually) // get rid of things
											# continue prevents from getting nested really far in 
		total += len(line)					# processing here // program here
		for i in range(len(aas)):
			aa = aas[i]
			caa[i] += line.count(aa)
#				c = line.count(aa)			# here's a line; let's count it with animo acids 
				#print(aa, c)
print(caa)

# iterating through the counts of the amino acids and going through the sequence




# Strat 4#
# use string.find 
# using that position 8, increase the number for that aa


## Notes ##
# compressed in gcf_......faa.gz; can open and redirect output ???
# count every letter and determine fraction of every single amino acid (count letter/divide by length of total genome) 
#	- how often does each one occur 
#	- look at the sequence line and count of all the letters 
#	- if line starts with > continue 



"""
python3 40aacomp.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz
A 126893 0.0954
C 15468 0.0116
D 68213 0.0513
E 76890 0.0578
F 51796 0.0389
G 97830 0.0736
H 30144 0.0227
I 79950 0.0601
K 58574 0.0440
L 142379 0.1071
M 37657 0.0283
N 51896 0.0390
P 59034 0.0444
Q 59178 0.0445
R 73620 0.0554
S 76865 0.0578
T 71428 0.0537
V 94237 0.0709
W 20297 0.0153
Y 37628 0.0283
"""
