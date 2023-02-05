# https://www.acmicpc.net/problem/1911

'''
input)
3 3
1 6
13 17
8 12

ans)
5
'''
import sys
import math
N, L = map(int, sys.stdin.readline().split())
water = []
for _ in range(N):
    s, e = map(int, sys.stdin.readline().split())
    water.append([s, e])

water.sort(key=lambda x:x[1])
cache = []
for i in range(len(water)):
    start, end = water[i][0], water[i][1]
    
    if i == 0:
        cache.append([start, end])
        continue

    if start <= cache[-1][1]:
        cache[-1][0] = min(cache[-1][0], start)
        cache[-1][1] = end
    else:
        cache.append([start, end])

ans = 0
last_covered = 0
for w in cache:
    start, end = w[0], w[1]

    if start < last_covered:
        start = last_covered

    new = math.ceil((end - start) / L)
    last_covered = start + new * L
    ans += new
print(ans)
