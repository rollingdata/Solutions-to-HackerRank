# -*- coding: utf-8 -*-
"""
Created on Sat May 26 22:18:30 2018

@author: januszhou
"""



def split_and_join(line):
    s = line.split()
    s = '-'.join(s)
    return(s)
    
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
