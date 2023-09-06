# https://www.acmicpc.net/problem/2217

'''
처음 틀렸던 것 반례 (끝까지 다 확인해봐야하는 이유)
input)
5
2
3
4
5
11

output)
11

ans)
12
'''

import sys

N = int(sys.stdin.readline())

data = [int(sys.stdin.readline()) for _ in range(N)]

data.sort(reverse=True)

value = 0
for i in range(len(data)):
    K = i + 1
    new_value = K * data[i]
    value = max(value, new_value)

print(value)