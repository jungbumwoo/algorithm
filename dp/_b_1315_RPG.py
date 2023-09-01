# https://www.acmicpc.net/problem/1315

# fix: 예제는 맞았으나 틀린 case 발생

import sys
sys.setrecursionlimit(10 ** 7)

N = int(sys.stdin.readline())

quests = []
for _ in range(N):
    s, i, p = map(int, sys.stdin.readline().split())
    quests.append([s, i, p, False]) # STR, INT, POINT, IS_COMPLETED

cache = {}

def beat(j, k, bits):
    if (j, k, bits) in cache:
        return cache[(j, k, bits)]

    get_point = 0
    new_success = []
    new_cnt = 0
    for t in range(len(quests)):
        s, i, p, is_completed = quests[t][0], quests[t][1], quests[t][2], quests[t][3]

        if is_completed:
            continue

        if j >= s or k >= i:
            new_success.append(t)
            new_cnt += 1
            quests[t][3] = True
            bits = bits & 1 << t
            get_point += p

    if get_point == 0:
        return 0
    
    new_cnt += max(beat(min(1000, j + get_point), k, bits), beat(j, min(1000, k + get_point), bits))

    for u in new_success:
        quests[u][3] = False
        bits = bits ^ 1 << u

    cache[(j, k, bits)] = new_cnt
    return new_cnt

print(beat(1, 1, 0))
