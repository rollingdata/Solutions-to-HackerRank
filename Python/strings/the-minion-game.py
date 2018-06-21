# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 21:03:22 2018

@author: januszhou
"""

def minion_game(string):
    vowels = 'AEIOU'
    stuart, kevin, ln = 0, 0, len(string)

    # directly count the number of possible combinations in the rest of the string
    for i in range(ln):  
        if string[i] in vowels:
            kevin += ln - i
        else:
            stuart += ln - i

    if stuart > kevin:
        print('Stuart', stuart)
    elif stuart == kevin:
        print('Draw')
    else:
        print('Kevin', kevin)
    
if __name__ == '__main__':
    s = input()
    minion_game(s)