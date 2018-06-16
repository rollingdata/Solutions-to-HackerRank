# -*- coding: utf-8 -*-
"""
Created on Sun May 27 17:11:28 2018

@author: januszhou
"""

def mutate_string(string, position, character):
    string_list = list(string)
    string_list[position] = character
    final_string = ''.join(string_list)
    
    return final_string



if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)