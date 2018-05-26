# -*- coding: utf-8 -*-
"""
Created on Sat May 26 16:41:33 2018

@author: januszhou
"""

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[i ,j , k] for i in range(x + 1) \
           for j in range(y + 1) \
           for k in range(z + 1) \
           if (i +j + k != n)])