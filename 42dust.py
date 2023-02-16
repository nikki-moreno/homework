# 42dust.py

# Nikki Moreno
# MCB 185
# 16 February 2023

## Purpose ##
# Write a program that performs entropy filtering on nucleotide fasta files
# Windows that are below the entropy threshold are replaced by N
# Program arguments include file, window size, and entropy threshold
# Output should be a fasta file with sequence wrapped at 60 characters
# Hint: use the mcb185 library
# Hint: make up some fake sequences for testing
# Note: don't worry about "centering" the entropy on the window (yet)




## Notes ##
# what's the similarity between two things? 
# take areas with low complexity
# need a generally similar answer but not the same
# change threshold value chooses what you can mask 
# Strategy 1; compute entropy of the window newly, over and over
# Strategy 2; how many ACTG in each window, 
	# calculate entropy calculation
	# fail means you can operate on them since they have non-zero values 

# Window size 10
# 5 As = 0.5 
# 5 Cs = 0.5
# Entropy = H 

"""
python3 42dust.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 11 1.4
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGNTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTNNNNNNNAAAAAGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGNNNNNNNNNNNATTTTATTGACTTAGG
TCACNNAATACTTTAACCAATATAGGCATAGCGCACAGNCNNNNAAAAATTACAGAGTNN
ACAACATCCATGAAACGCATTAGCACCACCATNNNNNNNACCATCACCATTACCACAGGT
AACNGTGCGGGCTGACGCGTACAGNNNNNNNNGAAAAAAGCCCGCACCTGACAGTGCNNN
NNNTTTTTTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
ANNCANGGGCAGGTGGCCANCGNNNNNNNTNNNCCCGNNNNNNNNNCCAACCACCTGGTG
GCGATNATTGNNAAAACCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
...
"""
