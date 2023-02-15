# 30stats.py

# Nikki Moreno
# 8 February 2023 - 14 February 2023
# MCB 185

## Purpose ##
# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# Hint: use sys.argv to get the values from the command line
# Note: you are not allowed to import any library except sys


# Import, container. desired input, and sort
import sys 
nums = []								# list			 
for val in sys.argv[1:]:				# every desired val will be appended into numbs
	nums.append(float(val))				# val type will go from str --> float
nums.sort()								# sorting for later; work smarter not harder!	

#print(nums)							- Note: is the list capturing what you want? 
	


# Count, Minimum, Maximum
length = len(nums)
print('Count: ', length)				# length of the list 
print('Minimum: ', nums[0])				# position 0 of the sorted list 
print('Maximum: ', nums[-1])			# count backwards from the sorted list 



# Mean
avg = sum(nums)/length	
print('Mean: ', f'{avg:.3f}')	




# Variance --> Standard Deviation
var = 0
for i in nums:
	var = var + ((i - avg) ** 2)
stddv = (var/length)** 0.5
print('Std. dev:', f'{stddv:.3f}')




# Median if even or odd, respectively 
if length % 2 == 0:							# if even, find mid
	mid = length/2							# mid returns a position
	median = (nums[mid] + nums[mid-1])/2	# median returns an index
else:
	mid = int((length/2) - 0.5)				# if odd, find mid position and round down
	median = nums[mid]						# median returns an index
print('Median:', f'{median:.3f}')


"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""