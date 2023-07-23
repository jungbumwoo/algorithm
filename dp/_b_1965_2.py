# 답은 맞았는데 개선여지 있음. 공간복잡도 개선가능
import sys

'''
8
1 6 2 5 7 3 5 6

10
1 2 3 4 5 6 7 8 9 10
'''

N = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))

if N == 1:
    print(1)
    sys.exit(1)

dp = list([[0, 0], [0, 0]] for _ in range(N))

dp[0][0][0], dp[0][0][1] = data[0], 1

for i in range(1, N):
    temp = 0
    for j in range(i, -1, -1):
        if data[j] < data[i]:
            temp = max(temp, dp[j][0][1])
    dp[i][0][0] = data[i]
    dp[i][0][1] = temp + 1

    if dp[i-1][0][1] > dp[i-1][1][1]:
        dp[i][1][0] = dp[i-1][0][0]
        dp[i][1][1] = dp[i-1][0][1]
    elif dp[i-1][0][1] < dp[i-1][1][1]:
        dp[i][1][0] = dp[i-1][1][0]
        dp[i][1][1] = dp[i-1][1][1]
    else: # same
        dp[i][1][0] = min(dp[i-1][0][0], dp[i-1][1][0])
        dp[i][1][1] = dp[i-1][0][1]

print(max(dp[-1][0][1], dp[-1][1][1]))
