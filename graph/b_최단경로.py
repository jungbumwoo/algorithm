import sys
import heapq
import math

from collections import defaultdict

# FIXME: 시간초과

'''
input
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6
'''

INF = math.inf

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

d = defaultdict(list)
data = [INF] * (V + 1)

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    d[u].append([w, u, v])

queue = list()
heapq.heapify(queue)
data[K] = 0

def enqueue(queue, s):
    for routes in d[s]:
        heapq.heappush(queue, routes)

enqueue(queue, K)
while queue:
    route = heapq.heappop(queue)
    weight, start, end = route[0], route[1], route[2]

    if data[start] + weight < data[end]:
        data[end] = data[start] + weight
        enqueue(queue, end)

for i in range(1, len(data)):
    if data[i] == INF:
        print("INF")
    else:
        print(data[i])
