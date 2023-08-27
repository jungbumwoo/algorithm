import heapq
import sys

# fixme: Kruskal 로 풀다가 틀림

'''
input)
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

result)
23
'''

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

queue = list()
heapq.heapify(queue)

parent = [i for i in range(N + 1)]


def find(i):
    if i == parent[i]:
        return i    
    return find(parent[i])


def union(x, y):
    x_parent = find(x)
    y_parent = find(y)

    if x_parent > y_parent:
        parent[y_parent] = x_parent
    elif y_parent > x_parent:
        parent[x_parent] = y_parent
    else:
        raise ValueError(f"Unexpected Case: x: {x_parent}, y: {y_parent}")

    return

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    heapq.heappush(queue, (c, a, b))

ans = 0

while queue:
    popped = heapq.heappop(queue)
    weight, start, end = popped[0], popped[1], popped[2]

    if find(start) != find(end):
        ans += weight
        union(start, end)

print(ans)
