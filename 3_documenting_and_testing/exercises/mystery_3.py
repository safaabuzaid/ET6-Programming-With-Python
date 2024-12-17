"""
The module return the smaller number, if the inputs are equal it return the sum of them.

Parameters:
two integers

Return:
the smaller number, f(equals)>summation of them

Examples:
>>> mystery_3(4,1)
1

>>> mystery_3(4,7)
4

>>> mystery_3(4,4)
8
"""

def mystery_3(a, b):
    if a < b:
        return a
    elif a > b:
        return b
    else: 
        return a + b
