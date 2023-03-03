# https://www.acmicpc.net/problem/1695

'''
앞에서 뒤로 보나, 뒤에서 앞으로 보나 같은 수열을 팰린드롬 이라고 한다. 
예를 들어 {1}, {1, 2, 1}, {1, 2, 2, 1}과 같은 수열은 팰린드롬 이지만, {1, 2, 3}, {1, 2, 3, 2} 등은 팰린드롬이 아니다.
한 수열이 주어졌을 때, 이 수열에 최소 개수의 수를 끼워 넣어 팰린드롬을 만들려고 한다. 최소 몇 개의 수를 끼워 넣으면 되는지를 알아내는 프로그램을 작성하시오.

input:
5
1 2 3 4 2

2 4 3 2 1
ans:
2
'''

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
data = [[0] * (len(arr) + 1) for _ in range(len(arr) + 1)]

for i in range(len(arr)):
    for j in range(len(arr)):
        k = len(arr) - j - 1

        if arr[i] == arr[k]:
            data[i+1][j+1] = data[i][j] + 1
        else:
            data[i+1][j+1] = max(data[i+1][j], data[i][j+1])

print(N - data[-1][-1])