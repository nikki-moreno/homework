### ide1_sequence-program.py

### Nikki Moreno
### MCB185 IDE1 (increasingly difficult exam) part 2
### 31 January 2023

### Purpose: A test to see where we are at in class. Make a sequence program.


# 1. Write a program that generates a DNA sequence n letter long with x 
# percentage GCs. For example, a sequence 10,000 long with 59.41% GC content. 

import random

n = 25
x = 0.53
seq =''

# generate random sequence
for i in range(n):
	r = random.random()
	if r < x: seq += random.choice('CG')
	else: 		seq += random.choice('AT')

# count letters
a = 0
c = 0
g = 0
t = 0
for nt in seq:
	if   nt == 'A': a += 1
	elif nt == 'C': c += 1
	elif nt == 'G': g += 1
	else:			t += 1

print(a/len(seq), c/len(seq), g/len(seq), t/len(seq))


# see if you can complete this and understand it...
'''
#kmers
print(seq)
k = 3
for i in range(len(seq) -k +1):
	k2 = k // 2
	kmer = seq[i:i+k]
	first = kmer[:k2]
	second = kmer[-k2:]
	rc = ''
	for nt in second:
		if nt == 'A': rc = 'T' 
		''
		''
	if first == revcomp(second): print('*')	

#palendrome
k2 = k // 2
print(k2)
print(test[0:k2], test[-k2:])
'''