# -*- coding: utf-8 -*-
"""
Created on Sun May 27 19:32:06 2018

@author: januszhou
"""

n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
# put the cone, welcome message and the reversed cone together
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))