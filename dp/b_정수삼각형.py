# https://www.acmicpc.net/problem/1932

import sys
N = int(sys.stdin.readline())
data = []
for _ in range(N):
    arr = list(map(int, sys.stdin.readline().split()))
    data.append(arr)

cache = [[0] * N, [0] * N]
cache[0][0] = data[0][0]

for i in range(1, N):
    k = i % 2
    before = (i-1) % 2

    for j in range(i+1):
        if j == 0:
            cache[k][j] = cache[before][j] + data[i][j]
        elif j == i:
            cache[k][j] = cache[before][j-1] + data[i][j]
        else:
            cache[k][j] = max(cache[before][j-1], cache[before][j]) + data[i][j]

print(max(cache[(N+1) % 2]))