# -*- coding: utf-8 -*-
"""
Created on Sat May 12 02:27:44 2018

@author: januszhou
"""

if __name__ == '__main__':
    n = int(input())
    
    # need to know how many digits for the element that needs to be appended
    
    result = 0
    for i in range(n + 1):
        # define temporary var to identify the number of digits in each loop
        length = 0
        temp = 1
        while (temp <= i):
            length += 1
            temp *= 10
        # multiply and do the summation
        result = result * (10 ** length)  + i
        
    print(result)