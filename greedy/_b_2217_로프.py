# https://www.acmicpc.net/problem/2217

import sys

N = int(sys.stdin.readline())

data = [int(sys.stdin.readline()) for _ in range(N)]

data.sort(reverse=True)
print(data)

value = 0
for i in range(len(data)):
    K = i + 1
    new_value = K * data[i]

    if new_value < value:
        print(value)
        sys.exit(0)

    value = new_value

print(value)