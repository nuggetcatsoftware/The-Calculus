from math import *
import math
def f(x): #simple multiplication bruh
    return x ** 2
def derive(function, value):
    h = 0.00000000001
    top = function(value + h) - function(value)
    bottom = h
    slope = top / bottom
    # Returns the slope to the third decimal
    return float("%.3f" % slope)

def euler(n):
    t_sum = 0
    for i in range(n):
        term = 1/math.factorial(i)
        t_sum = t_sum + term
    
    return t_sum

# Reading number of terms to be considered in series
terms = int(input("Enter number of terms: "))

# Function call
e = euler(terms)

# Displaying result
print("e = ", e)