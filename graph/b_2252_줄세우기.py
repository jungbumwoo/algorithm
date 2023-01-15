# https://www.acmicpc.net/problem/2252

'''
N명의 학생들을 키 순서대로 줄을 세우려고 한다. 각 학생의 키를 직접 재서 정렬하면 간단하겠지만, 마땅한 방법이 없어서 두 학생의 키를 비교하는 방법을 사용하기로 하였다. 
그나마도 모든 학생들을 다 비교해 본 것이 아니고, 일부 학생들의 키만을 비교해 보았다.
일부 학생들의 키를 비교한 결과가 주어졌을 때, 줄을 세우는 프로그램을 작성하시오.
'''

'''
ex 1)
3 2
1 3
2 3

ans)
1 2 3

ex 2)
4 2
4 2
3 1

ans 2)
4 2 3 1
'''
import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())
cnt = [0] * (N+1)
data = {}
queue = deque()

for _ in range(M):
    front, end = map(int, sys.stdin.readline().split())
    cnt[front] += 1
    if end not in data:
        data[end] = [front]
    else:
        data[end].append(front)

for i in range(1, len(cnt)):
    if cnt[i] == 0:
        queue.append(i)

ans = [0] * N
index = -1
while queue:
    student = queue.popleft()
    ans[index] = student
    index -= 1

    if student in data:
        for k in data[student]:
            cnt[k] -= 1
            if cnt[k] == 0:
                queue.append(k)

for p in ans:
    print(p, end=' ')