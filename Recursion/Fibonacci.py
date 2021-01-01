# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 21:54:30 2021

@author: Hanan Sheikh
"""

# #####################################
# # EXAMPLE:  fibonacci
# #####################################

def fib(x):
    """assumes x an int >= 0
        returns Fibonacci of x"""
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)
#an examble to test 
print(fib(7))