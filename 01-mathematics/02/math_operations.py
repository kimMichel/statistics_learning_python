import math

def power(base, exponent):
    return base ** exponent

def square_root(value):
    if value < 0:
        raise ValueError("Cannot compute square root of a negative number")
    return math.sqrt(value)

def logarithm(value, base=math.e):
    if value <= 0:
        raise ValueError("Cannot compute logarithm of a non-positive number")
    
    if base <= 0 or base == 1:
        raise ValueError("Logarithm base must be positive and not equal to 1")
    return math.log(value, base)

def scientific_notation(value):
    return "{:e}".format(value)