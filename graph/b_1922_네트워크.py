# fixme: wrong answer

import heapq
import sys

'''
6
9
1 2 5
1 3 4
2 3 2
2 4 7
3 4 6
3 5 11
4 5 3
4 6 8
5 6 8
'''

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

data = {}
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    if a not in data:
        data[a] = []
    if b not in data:
        data[b] = []
    data[a].append((b, c))
    data[b].append((a, c))

if N == 1:
    print(0)
    sys.exit(1)


picked = set()
queue = []
heapq.heapify(queue)


def select(num: int):

    for element in data[num]:
        depart, cost = element[0], element[1]

        if depart not in picked:
            heapq.heappush(queue, (cost, depart))

picked.add(1)
select(1)
result = 0

while queue:
    cost, computer = heapq.heappop(queue)
    picked.add(computer)
    result += cost

    select(computer)

print(result)



