import heapq
import sys

# fix: 백준 이슈임. 코드 수정없이 실행하면 또 정답처리됨. -> 그게 아니라 처음 틀렸을때 마지막줄 print를 누락하였음..

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


'''
pypy3로는 정답되고 python3로는 시간초과 나던 이슈 해결.

이 문제의 경우에 각 정점마다 parent, child 관계를 남길 필요가 없어서
매번 재귀로 부모를 찾아가기보다 각 연결된 정점이 직접 연결되지 않는 부모를 직접 참조하는 것이 효율적임.

def find(i):
    if i == parent[i]:
        return i    
    return find(parent[i])
'''

def find(i):
    if i != parent[i]:
        parent[i] = find(parent[i])    
    return parent[i]


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
