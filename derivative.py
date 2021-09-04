from math import *
def f(x): #simple multiplication bruh
    return x ** 2
def derive(function, value):
    h = 0.00000000001
    top = function(value + h) - function(value)
    bottom = h
    slope = top / bottom
    # Returns the slope to the third decimal
    return float("%.3f" % slope)