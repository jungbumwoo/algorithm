# https://www.acmicpc.net/problem/8980

'''
input)
6 5
6
5 6 2
4 5 3
1 2 2
3 6 2
3 4 3
2 6 1

output)
12


input)
5 5
4
2 3 2
2 5 3
3 4 1
2 4 1

output)
6

input)
5 4
7
2 5 4
3 4 1
1 4 4
1 5 3
3 5 1
2 3 3
1 2 3

output)
9
'''

import sys

from collections import defaultdict, OrderedDict

N, C = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())

data = defaultdict(list)

for _ in range(M):
    s, e, c = map(int, sys.stdin.readline().split())

    data[s].append([e, c])

truck = dict()

ans = 0
for i in range(1, N + 1):

    # 배송완료
    if i in truck:
        ans += truck[i]
        del truck[i]

    # 담기
    for k in range(len(data[i])):
        arrive, count = data[i][k][0], data[i][k][1]

        if arrive in truck:
            truck[arrive] += count
        else:
            truck[arrive] = count

    # 무게초과 난거 버려
    is_done = False
    spare = C
    for key, value in sorted(truck.items()):
        if spare > value:
            spare -= value
        elif spare <= value:
            truck[key] = spare
            spare = 0
            if_done = True
        elif is_done is True:
            del truck[key]
    
print(ans)


