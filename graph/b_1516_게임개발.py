import sys
from collections import deque

n = int(sys.stdin.readline())
indegree =[0 for _ in range(n+1)]
time =[0 for _ in range(n+1)]
graph = [[] for _ in range(n+1)]
answer = [0 for _ in range(n+1)]
que = deque()
for i in range(n):
    input = list(map(int, sys.stdin.readline().split()))
    indegree[i+1] = len(input)-2
    time[i+1] = input[0]
    for j in input[1:-1]:
        graph[j].append(i+1)

for i in range(1, n+1):
    if indegree[i] == 0:
        que.append(i)

while que:
    now = que.popleft() # B
    answer[now] += time[now] # B <- B
        
    for node in graph[now]:
        indegree[node] -= 1
        answer[node] = max(answer[node], answer[now]) 
        if indegree[node] == 0:
            que.append(node)

for i in range(1,n+1):
    print(answer[i])