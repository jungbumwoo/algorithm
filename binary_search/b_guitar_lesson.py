'''
Link: https://www.acmicpc.net/problem/2343

input
9 3
1 2 3 4 5 6 7 8 9
'''
import sys

N, M = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))

start = max(data)
end = sum(data)
result = end

while start <= end:
    mid = (start + end) // 2
    if mid < max(data):
        start = mid + 1
        continue

    temp, cnt = 0, 1
    
    for i in range(len(data)):
        if temp + data[i] <= mid:
            temp += data[i]
        else:
            cnt += 1
            temp = data[i]

    if cnt <= M:
        end = mid - 1
        result = min(mid, result)
    else:
        start = mid + 1
    
print(result)


