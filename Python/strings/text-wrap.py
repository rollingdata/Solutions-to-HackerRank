# -*- coding: utf-8 -*-
"""
Created on Sun May 27 18:10:21 2018

@author: januszhou
"""

import textwrap

def wrap(string, max_width):
    output = '\n'.join(textwrap.wrap(string, max_width))
    return(output)
    
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)