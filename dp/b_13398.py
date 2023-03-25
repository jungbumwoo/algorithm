# Link : https://www.acmicpc.net/problem/13398

'''
input)
10
10 -4 3 1 5 6 -35 12 21 -1
'''

import sys
sys.setrecursionlimit(10**6)
import functools

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

ans = [None]

@functools.lru_cache(maxsize=None)
def pick(i, already=False):
    print(i, already)
    if i == len(data):
        return 0
    
    if already:
        nxt = pick(i + 1, True)
        t = nxt + data[i]
        if t < 0:
            return 0
        else:
            if ans[0] is None:
                ans[0] = t
            else:
                ans[0] = max(ans[0], t)

            return t
    else:
        nxt = pick(i + 1, False)
        p = nxt + data[i]

        nxt = pick(i + 1, True)
        q = nxt
        
        temp = max(p, q)

        if temp > 0:
            if ans[0] is None:
                ans[0] = temp
            else:
                ans[0] = max(temp, ans[0])
            return temp
        else:
            return 0


# if N == 1:
#     print(max(data))
#     sys.exit(1)

pick(0, False)

if ans[0] is None:
    print(max(data))
else:
    print(ans[0])
