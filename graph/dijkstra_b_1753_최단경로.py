'''
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
'''

import heapq
import math
import sys

from collections import defaultdict


V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

cost = [math.inf] * (V + 1)

routes = defaultdict(list)

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    routes[u].append((w, v))

queue = []
heapq.heapify(queue)

cost[K] = 0
for route in routes[K]:
    heapq.heappush(queue, route)

while queue:
    r = heapq.heappop(queue)
    weight, arrived_at = r[0], r[1]

    if weight < cost[arrived_at]:
        cost[arrived_at] = weight

        for route in routes[arrived_at]:
            next_cost, next_arrive = route[0], route[1]

            if weight + next_cost < cost[next_arrive]:
                heapq.heappush(queue, (next_cost, next_arrive))

for k in range(1, len(cost)):
    if cost[k] == math.inf:
        print('INF')
    else:
        print(cost[k])
