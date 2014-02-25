# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

def bigger(a,b):   #return bigger input of two inputs
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):                 
    return bigger(a,bigger(b,c))    #return biggest of three inputs: input a, and bigger of b and c

def median(a,b,c):
    big = biggest(a,b,c)            
    if big == a:              # if a is biggest of three inputs
        return bigger(b,c)    # return the bigger of the remaining two inputs 
    if big == b:              # if b is biggest of three inputs
        return bigger(a,c)    # return the bigger of a, c
    if big ==c:               # if c is biggest of three inputs
        return bigger(a,b)    # return bigger of a, b


print(median(1,2,3))
>>> 2

print(median(9,3,6))
>>> 6

print(median(7,8,7))
>>> 7

    