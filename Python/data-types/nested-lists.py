# -*- coding: utf-8 -*-
"""
Created on Sat May 26 18:16:52 2018

@author: januszhou
"""

if __name__ == '__main__':
    # nested input, actually not suggested
    student_records = [[input(), float(input())] for _ in range(int(input()))]
        
    # need to find the second lowest score
    # set will sort the scores automatically
    # fetch scores and put them in a list
    second_lowest_score = sorted(list(set([score for name, score in student_records])))[1]
    
    # then output the correspoding names alphabetically
    print('\n'.join([a for a,b in sorted(student_records) if b == second_lowest_score]))