# -*- coding: utf-8 -*-
"""
Created on Sun May 27 17:44:26 2018

@author: januszhou
"""

if __name__ == '__main__':
    s = input()

    for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:
        print(any(method(c) for c in s))
