# Link : https://www.acmicpc.net/problem/1958

'''
input)
abcdefghijklmn
bdefg
efg
'''

import sys

data1 = sys.stdin.readline().rstrip()
data2 = sys.stdin.readline().rstrip()
data3 = sys.stdin.readline().rstrip()

dp = [[[0] * (len(data3) + 1) for _ in range(len(data2) + 1)] for _ in range(len(data1) + 1)]
ans = 0
for i in range(1, len(data1) + 1):
    for j in range(1, len(data2) + 1):
        for k in range(1, len(data3) + 1):
            if data1[i-1] == data2[j-1] == data3[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
                ans = max(ans, dp[i][j][k])
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

print(ans)