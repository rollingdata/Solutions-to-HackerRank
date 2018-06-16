# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 15:46:23 2018

@author: januszhou
"""




"""
this function takes in an size input and print out the following patterns

e.g. input 5

--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""

import string

def print_rangoli(size):

    alpha = string.ascii_lowercase

    n = int(input())
    L = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        # combining upper and lower part
        L.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    
    print('\n'.join(L[:0:-1]+L))
    


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)