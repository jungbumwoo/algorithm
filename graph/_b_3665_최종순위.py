

'''
fixme: convert 로 들어오는 순서가 우선순위 기준으로 들어오는 보장이 없다.

1
3
1 3 2
1
1 3

output)
IMPOSSIBLE

ans)
3 1 2

----------------------------------------------------------------
1
2
1 2
1
1 2
IMPOSSIBLE

ans)
2 1
'''

import sys
from collections import deque, defaultdict

N = int(sys.stdin.readline())

for _ in range(N):
    K = int(sys.stdin.readline())
    order = list(map(int, sys.stdin.readline().split()))
    P = int(sys.stdin.readline())

    converts = []
    for _ in range(P):
        a, b = map(int, sys.stdin.readline().split())
        converts.append([a, b])

    dicts = defaultdict(set)
    nums = [0] * (len(order) + 1)
    for i in range(len(order)):
        for j in range(i+1, len(order)):
            first, second = order[i], order[j]

            if first not in dicts:
                dicts[first] = set()
            dicts[first].add(second)
            nums[second] += 1

    err_flag = False
    for k in range(len(converts)):
        p, q = converts[k][0], converts[k][1]

        try:
            dicts[q].remove(p)
        except KeyError:
            err_flag = True
        nums[p] -= 1

        dicts[p].add(q)
        nums[q] += 1

    if err_flag:
        print("IMPOSSIBLE")
        continue

    queue = deque()
    for t in range(1, len(order)+ 1):
        if nums[t] == 0:
            queue.append(t)

    ans = []
    while queue:
        A = queue.popleft()
        ans.append(str(A))

        for element in dicts[A]:
            nums[element] -= 1

            if nums[element] == 0:
                queue.append(element)

    if len(ans) != len(order):
        print("IMPOSSIBLE")
    else:
        print(" ".join(ans))
