# -*- coding: utf-8 -*-
"""
Created on Sat May 26 18:32:42 2018

@author: januszhou
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    output_percentage = sum(student_marks[query_name]) / len(student_marks[query_name])
    # print format control
    print('%.2f' % output_percentage)