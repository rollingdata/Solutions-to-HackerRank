# -*- coding: utf-8 -*-
"""
Created on Sat May 26 17:06:31 2018

@author: januszhou
"""

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    # remove duplicates
    arr = list(set(arr))
    winner_score = max(arr)
    arr.remove(winner_score)
    runner_score = max(arr)
    print(runner_score)