# -*- coding: utf-8 -*-
"""
Created on Sat May 26 16:40:44 2018

@author: januszhou
"""

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))