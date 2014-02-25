# Given a variable, x, that stores the 
# value of any decimal number, write Python 
# code that prints out the nearest whole 
# number to x.
# If x is exactly half way between two 
# whole numbers, round up, so
# 3.5 rounds to 4 and 2.5 rounds to 3.
# You may assume x is not negative.

print int(float(x + 0.5))

x = 3.14159 
>>> 3 
x = 27.63 
>>> 28 (not 28.0)
x = 3.5 
>>> 4 (not 4.0)

#x = 3.14159
