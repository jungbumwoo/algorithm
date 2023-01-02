# https://www.acmicpc.net/problem/1806

'''
문제 : 
10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 
이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오.

입력값 :
첫째 줄에 N (10 ≤ N < 100,000)과 S (0 < S ≤ 100,000,000)가 주어진다. 둘째 줄에는 수열이 주어진다. 
수열의 각 원소는 공백으로 구분되어져 있으며, 10,000이하의 자연수이다.

예)
10 15
5 1 3 5 10 7 4 9 2 8

답) 
2
'''
import sys
N, S = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

if S == 0:
    print(0)
    sys.exit()

left, right = 0, 0
total = data[0]
ans = 10 ** 9

while right < len(data) and left <= right:
    if total >= S:
        ans = min(ans, right - left + 1)
        total -= data[left]
        left += 1
    else:
        right += 1
        if right < len(data):
            total += data[right]

if ans == 10 ** 9:
    print(0)
else:
    print(ans)
        