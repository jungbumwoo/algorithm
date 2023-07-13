# https://www.acmicpc.net/problem/10815

'''
input
5
6 3 2 10 -10
8
10 9 -5 2 3 4 5 -10
'''

import sys

N = int(sys.stdin.readline())
cards = set(map(int, sys.stdin.readline().split()))

_ = int(sys.stdin.readline())

for c in map(int, sys.stdin.readline().split()):
    if c in cards:
        print(1, end=' ')
    else:
        print(0, end=' ')
