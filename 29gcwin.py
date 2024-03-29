# 29gcwin.py

# Nikki Moreno
# 5 February 2023
# MCB 185

## Purpose ##
# Write a program that computes the GC fraction of a DNA sequence in windows
# Window size is 11 nt
# Output with 4 significant figures
# Try this with nested loops first
# Variation: try programming this without nested loops
# Instead, count only the first window
# Then 'move' the window by adding 1 letter on one side
# And subtracting 1 letter from the other side
# Consider the pros/cons of this algorithm vs. nested loops




## sequence, window size and initial variables ##

seq = 'ACGACGCAGGAGGAGAGTTTCAGAGATCACGAATACATCCATATTACCCAGAGAGAG'
w = 11
# count = 0 					count will start at 1 after the first loops
# count = i 					i is not defined 
# gc = 0 						adds all of the gc through every loops ( ~ 22.1)   


## making the window and counting GCs with nested loops ##

for i in range(len(seq) -w +1): # length of the sequence minuse the window 	 
	count = i
	gc = 0						 # adds up only gc through a single loop 
	window = seq[i:i+w]			 # window length = 11
	for nt in window:  		 	 # for the nucleotides in the window
		if nt == 'G' or nt == 'C': gc = gc + 1
	print(f'{count} {window} {gc/len(window):.4f}')

'''
## making the window and counting GCs without nested loops ##

for i in range(len(seq) -w +1):
	count = i
	gc = 0
	window = seq[i:i+w]
	if i == 'G' or i == 'C': gc = gc + 1

	print(f'{count} {window} {gc/len(window):.4f}')
# still working on this one...

'''











# notes #
# first loop, moves the beginning position of the window
# second loop, once you have a window, it needs to count the letters inside it
'''
for i in range(len(seq) - w + 1):
	win = seq[i:i+w]
	for nt in win:
		if nt == 'G' or nt == 'C': .... 
	print(win)
'''
# i keeps going to the end, make sure you can stop 









"""
python3 26gcwin.py
0 ACGACGCAGGA 0.6364
1 CGACGCAGGAG 0.7273
2 GACGCAGGAGG 0.7273
3 ACGCAGGAGGA 0.6364
4 CGCAGGAGGAG 0.7273
5 GCAGGAGGAGA 0.6364
6 CAGGAGGAGAG 0.6364
7 AGGAGGAGAGT 0.5455
8 GGAGGAGAGTT 0.5455
9 GAGGAGAGTTT 0.4545
10 AGGAGAGTTTC 0.4545
11 GGAGAGTTTCA 0.4545
12 GAGAGTTTCAG 0.4545
13 AGAGTTTCAGA 0.3636
14 GAGTTTCAGAG 0.4545
15 AGTTTCAGAGA 0.3636
16 GTTTCAGAGAT 0.3636
17 TTTCAGAGATC 0.3636
18 TTCAGAGATCA 0.3636
19 TCAGAGATCAC 0.4545
20 CAGAGATCACG 0.5455
21 AGAGATCACGA 0.4545
22 GAGATCACGAA 0.4545
23 AGATCACGAAT 0.3636
24 GATCACGAATA 0.3636
25 ATCACGAATAC 0.3636
26 TCACGAATACA 0.3636
27 CACGAATACAT 0.3636
28 ACGAATACATC 0.3636
29 CGAATACATCC 0.4545
30 GAATACATCCA 0.3636
31 AATACATCCAT 0.2727
32 ATACATCCATA 0.2727
33 TACATCCATAT 0.2727
34 ACATCCATATT 0.2727
35 CATCCATATTA 0.2727
36 ATCCATATTAC 0.2727
37 TCCATATTACC 0.3636
38 CCATATTACCC 0.4545
39 CATATTACCCA 0.3636
40 ATATTACCCAG 0.3636
41 TATTACCCAGA 0.3636
42 ATTACCCAGAG 0.4545
43 TTACCCAGAGA 0.4545
44 TACCCAGAGAG 0.5455
45 ACCCAGAGAGA 0.5455
46 CCCAGAGAGAG 0.6364
"""
