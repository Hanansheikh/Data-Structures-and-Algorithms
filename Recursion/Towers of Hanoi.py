# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 21:52:43 2021

@author: Hanan Sheikh
"""


#####################################
# EXAMPLE:  Towers of Hanoi
#####################################

def printMove(fr, to):
    print('move from ' + str(fr) + ' to ' + str(to))

def Towers(n, fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n-1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n-1, spare, to, fr)

print(Towers(4, 'P1', 'P2', 'P3'))
