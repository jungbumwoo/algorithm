import sys
import heapq
import math

from collections import defaultdict

# FIXME: 시간초과
# FIXME: bfs 처럼 변경했으나 여전히 timeout
# FIXME: visited 넣었더니 틀려버림

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
visited = [False] * (V + 1)

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    d[u].append([w, v])

queue = list()
heapq.heapify(queue)

data[K] = 0
heapq.heappush(queue, [0, K])

while queue:
    route = heapq.heappop(queue)
    weight, now = route[0], route[1]

    if weight > data[now]:
        continue

    for next_point in d[now]:
        next_w, next_e = next_point[0], next_point[1]
        
        if next_w + data[now] < data[next_e]:
            data[next_e] = next_w + data[now]
            heapq.heappush(queue, [next_w, next_e])

for i in range(1, len(data)):
    if data[i] == INF:
        print("INF")
    else:
        print(data[i])
