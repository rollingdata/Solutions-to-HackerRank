# -*- coding: utf-8 -*-
"""
Created on Sat May 26 22:25:11 2018

@author: januszhou
"""

def print_full_name(a, b):
    first_name = a.capitalize()
    last_name = b.capitalize()
    print("Hello " + first_name + " "+ last_name + "! You just delved into python.")
    
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)