# https://www.acmicpc.net/problem/2231

import sys

N = int(sys.stdin.readline())

for i in range(N):

    str_num = str(i)
    li_num = list(str_num)
    temp = 0

    for j in li_num:
        temp += int(j)
    
    temp += i

    if temp == N:
        print(i)
        sys.exit(0)
print(0)
