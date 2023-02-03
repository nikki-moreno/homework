# 21codons.py

# Print out all the codons for the sequence below in reading frame 1

# Hint: use the slice operator

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'

for frame in range(3):      # for a variable in a specific range of integers
    for position in range(frame, len(dna) -2, 3):
        codon = dna[position:position+3]
        print(codon)
    print()

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
