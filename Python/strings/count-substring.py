# -*- coding: utf-8 -*-
"""
Created on Sun May 27 17:30:34 2018

@author: januszhou
"""

def count_substring(string, sub_string):
    # work with find and loop
    count = 0
    remaining_string = string
    while True:
        index = remaining_string.find(sub_string)
        if index != -1:
            remaining_string = remaining_string[(index + 1): ]
            count += 1
        else:
            break
    
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)