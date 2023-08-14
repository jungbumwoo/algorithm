import sys

# https://www.acmicpc.net/problem/12865

N, K = map(int, sys.stdin.readline().split())

'''
ex input)
4 7
6 13
4 8
3 6
5 12

ex ans)
14
'''
# Top-Down
data = []
for i in range(N):
    W, V = map(int, sys.stdin.readline().split())
    data.append((W, V))

cache = {}

def dfs(i: int, k: int):
    if i == len(data):
        return 0
    
    if (i, k) in cache:
        return cache[(i, k)]

    cache[(i, k)] = dfs(i + 1, k)
    if k - data[i][0] >= 0:
        cache[(i, k)] = max(dfs(i + 1, k - data[i][0]) + data[i][1], cache[(i, k)])

    return cache[(i, k)]

print(dfs(0, K))


# bottom - up
'''
data = []
for i in range(N):
    W, V = map(int, sys.stdin.readline().split())
    data.append((W, V))

dp = [[0] * (K + 1) for _ in range(N + 1)]
for i in range(1, N + 1):
    for j in range(1, K + 1):
        w, v = data[i - 1]

        if w > j:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        else:
            dp[i][j] = max(v + dp[i-1][j-w], dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
'''