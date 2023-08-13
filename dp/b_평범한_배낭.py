import sys

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
