# 28aapairs.py

# Nikki Moreno
# 5 February 2023
# MCB 185

## Purpose ##
# Print out all the unique pairwise amino acid combinations
# AC is the same as CA
# Skip AA, CC etc.
# Also print out how many combinations there are
# Hint: if you get stuck for more than 10 minutes, get help

 # set variable(s)
aa = 'ACDEFGHIKLMNPQRSTVWY'




'''
# this prints all possible combinations of amino acids
for i in aa:
	for j in aa:
		print(i,j)
'''

'''
# this prints all possible combinations of amino acids, with major diagonal
for i in range(0, len(aa)):
	for j in range(i, len(aa)):
		print(aa[i], aa[j])
'''

# this prints all unique amino acid combinations instead of unique positions
n = 0
for i in range(0, len(aa)):
	for j in range(i + 1, len(aa)):
		n = n + 1
		print(aa[i], aa[j])
print(n)


'''
# this prints all possible combinations of positions, with major diagonal
for i in range(0,len(aa)):
	for j in range(i, len(aa)):
		print(i,j)
'''


'''
# this prints unique positions instead of unique amino acids (no major diagonal)
for i in range(0, len(aa)):
	for j in range(i+1, len(aa)):
		print(i, j)
'''


'''
 # for j in range ( i+1, 4) without the major diagonal; 
 # not allowed to compare ny to ny
 # for j in range(i, 4) with major diagonal

'''
"""
python3 28aapairs.py
A C
A D
A E
A F
A G
A H
A I
A K
A L
A M
A N
A P
A Q
A R
A S
A T
A V
A W
A Y
C D
C E
C F
C G
C H
C I
C K
C L
C M
C N
C P
C Q
C R
C S
C T
C V
C W
C Y
D E
D F
D G
D H
D I
D K
D L
D M
D N
D P
D Q
D R
D S
D T
D V
D W
D Y
E F
E G
E H
E I
E K
E L
E M
E N
E P
E Q
E R
E S
E T
E V
E W
E Y
F G
F H
F I
F K
F L
F M
F N
F P
F Q
F R
F S
F T
F V
F W
F Y
G H
G I
G K
G L
G M
G N
G P
G Q
G R
G S
G T
G V
G W
G Y
H I
H K
H L
H M
H N
H P
H Q
H R
H S
H T
H V
H W
H Y
I K
I L
I M
I N
I P
I Q
I R
I S
I T
I V
I W
I Y
K L
K M
K N
K P
K Q
K R
K S
K T
K V
K W
K Y
L M
L N
L P
L Q
L R
L S
L T
L V
L W
L Y
M N
M P
M Q
M R
M S
M T
M V
M W
M Y
N P
N Q
N R
N S
N T
N V
N W
N Y
P Q
P R
P S
P T
P V
P W
P Y
Q R
Q S
Q T
Q V
Q W
Q Y
R S
R T
R V
R W
R Y
S T
S V
S W
S Y
T V
T W
T Y
V W
V Y
W Y
190
"""
