# -*- coding: utf-8 -*-
"""
Created on Sat May 26 16:17:05 2018

@author: januszhou
"""

if __name__ == '__main__':
    # specify the number of manipulations
    N = int(input())
    result_list = []
    for i in range(N):
        line_input = input().split(sep = ' ')
        # check over all possible command and convert index into integer
        if line_input[0] == 'insert':
            result_list.insert(int(line_input[1]), int(line_input[2]))
        elif line_input[0] == 'print':
            print(result_list)
        elif line_input[0] == 'remove':
            result_list.remove(int(line_input[1]))
        elif line_input[0] == 'append':
            result_list.append(int(line_input[1]))
        elif line_input[0] == 'sort':
            result_list.sort()
        elif line_input[0] == 'pop':
            if len(result_list) > 0:
                result_list.pop()
        elif line_input[0] == 'reverse':
            result_list.reverse()
        else:
            raise ValueError('Unrecognized command')
            
            
# another solution using 'eval'            
'''
n = input()
l = []
for _ in range(n):
    s = raw_input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        eval("l."+cmd)
    else:
        print l
'''