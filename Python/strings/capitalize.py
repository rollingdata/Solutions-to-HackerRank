# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 16:41:14 2018

@author: januszhou
"""

import math
import os
import random
import re
import sys


# Complete the solve function below.
def solve(s):
    elements = s.split()
    # capitals = list(map(lambda x: x.capitalize(), elements))
    return(' '.join(c.capitalize() for c in elements))
    
    
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
