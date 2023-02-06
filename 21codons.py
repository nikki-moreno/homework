# 21codons.py

# Nikki Moreno
# 4 February 2023
# MCB 185

### Purpose ###
# Print out all the codons for the sequence below in reading frame 1
# Hint: use the slice operator

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'

for ORF_1 in range(0, len(dna), 3): # establish ORF and step length
	codon = dna[ORF_1: ORF_1 + 3]   # codon defined by slice
	print(codon)
print()                             # new line after every step

"""
python3 21codons.py
ATA
GCG
AAT
ATC
TCT
CAT
GAG
AGG
GAA
"""
