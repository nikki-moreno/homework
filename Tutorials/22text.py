# 12text.py

# Move the triple quotes downward to uncover each segment of code



# Variables with text are called strings
"""
a = 'ACGT' # a string

# Square brackets let you access sub-strings as 'slices'
# Follow closely below, because the endpoints can be confusing
# The first number before : is the starting index, which starts at zero
# The second number after : is one larger than the last index

print(a, a[0], a[1])
print(a[2], a[2:3], a[2:4], a[2:5]) #a[2] = G = a[2:3]

# You can also do the following shortcuts

print(a[:2]) # the 0 is implict on the left
print(a[2:]) # the end of the string is implicit on the right

# The + operator concatenates strings

a = a + 'N'
a += 'n'   # note that += is a shorthand for s = s +, just like in math
print(a)

# The * operator repeats strings
a *= 3
print(a)


# The len() function returns the length of a string
# Some function like len() return values, others like print() do not

print(len(a))
"""
# There are several ways to format strings

txt = 'Ian'
num = 3/11

# Previously, we have used the print() function with commas

print([1], txt, num)

# What if we want to control the way the text looks?
# For example, what if we want exactly 3 decimal places?
# There are 3 distinct ways to format strings in python

# Method 1: f-strings, the best way
# f-strings are the newest and best way to format strings
# f-strings interpolate variables and other statements inside curly brackets

print([2], f'{txt} {num}')
print([3], f'{txt} {num:.3f}') # 3 digits of accuracy

# You can even interpolate python code

print([4], f'{2+2} {1/7:.5f} {len(txt)}')

"""
# The examples here are but the tip of a very large iceberg
# There are lots of formatting options!
# Use f-strings instead of the other methods below (included for completeness)

#---------------------------------------------------

# Method 2: printf-style formatting

print('%s %.3f' % (txt, num))                # %s string, %f float
print('%s %.3f %d %e' % (txt, num, 2.1, .1)) # %d integer, %e scientific

# Method 3: str.format()

print('{} {}'.format(txt, num))
print('{} {:.3f}'.format(txt, num))
"""

