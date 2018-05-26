# -*- coding: utf-8 -*-
"""
Created on Sat May 26 21:48:01 2018

@author: januszhou
"""

"""
This function is designed to flip the case of a string

"""

def swap_case(s):    
    swapped_string = ''.join([i.lower() if i.isupper() else i.upper() for i in s])
    return(swapped_string)

# Bulit-in method
#def swap_case(s):
#    return(s.swapcase())


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)