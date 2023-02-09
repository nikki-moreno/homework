# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list


"""
python3 33birthday.py 365 23
0.571
"""

## Notes ##
## 1st approach##
# bucket sort; linear
# faster way (maybe) but takes up more memory 
# days in a calender, length 365 (don't have to use 365 at the beginning)
# initialization with 0s .append
# random choice?
# create a random birthday and change that position to 1 from 0
# can do this 23 times 
# create empty year multiple times; checking probability so you need to do this
# process a bunch of times
# 	- setup the calender multiple times


## 2nd approach ##
# more like sorting, comparing individual values to each other after every step
# if the birthday is already in the list you've seen, [23, 47, 35, 23, etc] 
# interrigate each new number to see if 
# you've seen the number before 
# involving comparisons

## For Both Approaches##
# generate all the birthdays, then go through and check them
# OR
# generate and check them as you go 