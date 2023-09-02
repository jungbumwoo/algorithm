'''
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
'''

# fixme: memory 초과

import sys

N = int(sys.stdin.readline())
raw = []
parent = [i for i in range(N)]

def find(k):
    if k == parent[k]:
        return k
    parent[k] = find(parent[k])
    return parent[k]

def union(a, b):
    a_parent = find(a)
    b_parent = find(b)

    if a_parent == b_parent:
        raise ValueError('Unexpected Case. a, b have same parent')
    
    if a_parent < b_parent:
        parent[a_parent] = b_parent
    else:
        parent[b_parent] = a_parent


for _ in range(N):
    x, y, z = map(int, sys.stdin.readline().split())
    raw.append((x, y, z))

dists = []
for i in range(N):
    for j in range(i + 1, N):
        ax, ay, az = raw[i][0], raw[i][1], raw[i][2]
        bx, by, bz = raw[j][0], raw[j][1], raw[j][2]

        dist = min(abs(ax - bx), abs(ay - by), abs(az - bz))
        dists.append((dist, i, j))

dists.sort()

ans = 0
for d in dists:
    weight, start, end = d[0], d[1], d[2]

    if find(start) != find(end):
        ans += weight
        union(start, end)

print(ans)