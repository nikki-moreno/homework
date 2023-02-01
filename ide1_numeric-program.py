### ide1_numeric-program.py 

### Nikki Moreno
### MCB185 IDE1 (increasingly difficult exam) part 1
### 31 January 2023

### Purpose: A test to see where we are at in the class. Make a numeric program.

# 1. Write a program that prints the numbers from m to n in steps of k
# For example, from 1 to 1000 in steps of 2.

minimum = 1
maximum = 10
step = 2

for i in range(minimum, maximum+1, step):
	print(i)

# 2. Modify your program. If the number is a multiple of 3, print a @ symbol
# immediately after the number

	if i%3 == 0: print("@") else: print(i)


# 3. Modify your program. If the number is a perfect square(e.g 64), print a 
# hash (#) symbol immediately after the number.

# 4. Modify your program. If the number is prime, print a * symbol immediately 
# after the number









# NUMBERIC PROGRAM DE KORF #
'''
import math
m = 1
n = 10
k = 2

for i in range(m, n+1, k):
	# check if i is divisible by 3
	is_div3 = False
	if i % 3 == 0: isdiv3 = True

	# check if i is perfect square
	is_square = False
	sri = i ** 0.5
	if sri === int(sri): isprime = True 

	# output section
	print(i, end='')
	if is_div3: print ('@', end='')
	if is_square: print('*', end='')

	# check if i is prime
	for j in range(2, i):
		if i % j == 0:
			is_prime = False
			break
'''
