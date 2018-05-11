# -*- coding: utf-8 -*-
"""
Created on Sat May 12 01:26:22 2018

@author: januszhou
"""

if __name__ == '__main__':
    n = int(input())
    if n % 2 != 0 or (n >= 6 and n <= 20):
        print("Weird")
    else:
        print("Not Weird")