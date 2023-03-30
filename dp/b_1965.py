
'''
inputs)
8
1 6 2 5 7 3 5 6
ans = 5

10
1 2 3 4 5 6 7 8 9 10
ans = 10
'''

import functools
import sys
sys.setrecursionlimit(10 ** 6)

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

@functools.lru_cache(maxsize=None)
def pick(i, before):
    if i == len(data):
        return 0    
    a = 0
    if data[i] > before:
        a = pick(i + 1, data[i]) + 1

    b = pick(i + 1, before)

    return max(a, b)

print(pick(0, 0))
