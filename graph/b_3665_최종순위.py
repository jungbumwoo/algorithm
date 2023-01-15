# https://www.acmicpc.net/problem/3665

'''
올해 ACM-ICPC 대전 인터넷 예선에는 총 n개의 팀이 참가했다. 팀은 1번부터 n번까지 번호가 매겨져 있다. 놀랍게도 올해 참가하는 팀은 작년에 참가했던 팀과 동일하다.

올해는 인터넷 예선 본부에서는 최종 순위를 발표하지 않기로 했다. 그 대신에 작년에 비해서 상대적인 순위가 바뀐 팀의 목록만 발표하려고 한다. 
(작년에는 순위를 발표했다) 예를 들어, 작년에 팀 13이 팀 6 보다 순위가 높았는데, 올해 팀 6이 팀 13보다 순위가 높다면, (6, 13)을 발표할 것이다.

창영이는 이 정보만을 가지고 올해 최종 순위를 만들어보려고 한다. 작년 순위와 상대적인 순위가 바뀐 모든 팀의 목록이 주어졌을 때, 올해 순위를 만드는 프로그램을 작성하시오. 
하지만, 본부에서 발표한 정보를 가지고 확실한 올해 순위를 만들 수 없는 경우가 있을 수도 있고, 일관성이 없는 잘못된 정보일 수도 있다. 이 두 경우도 모두 찾아내야 한다.
'''


'''
ex)
3
5
5 4 3 2 1
2
2 4
3 4
3
2 3 1
0
4
1 2 3 4
3
1 2
3 4
2 3

ans)
5 3 2 4 1
2 3 1
IMPOSSIBLE
'''

import sys
from collections import deque
C = int(sys.stdin.readline())

for _ in range(C):
    N = int(sys.stdin.readline())
    dict = {}
    cnt = [0] * (N + 1)
    last_year = list(map(int, sys.stdin.readline().split()))
    
    for k in range(len(last_year)):
        cnt[last_year[k]] = len(last_year) - (k + 1) # 받는거
        dict[last_year[k]] = set(last_year[0:k]) # 나가는거
    
    M = int(sys.stdin.readline())

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        
        if a in dict[b]:
            high = a
            low = b
        else:
            high = b
            low = a

        cnt[high] -= 1
        cnt[low] += 1

        dict[high].add(low)
        dict[low].remove(high)
    
    queue = deque()

    for i in range(1, len(cnt)):
        if cnt[i] == 0:
            queue.append(i)
    if len(queue) == 0:
        print("IMPOSSIBLE")
        continue

    total = N
    flag = False
    ans = [0] * N
    index = -1

    while queue:
        if len(queue) > 1:
            flag = True

        team = queue.popleft()
        ans[index] = team
        index -= 1

        for element in dict[team]:
            cnt[element] -= 1
            if cnt[element] == 0:
                queue.append(element)

    if -(index + 1) == N:
        print(" ".join(map(str, ans)))
    else:
        print("IMPOSSIBLE")
