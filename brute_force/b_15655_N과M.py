'''
3 1
4 5 2

4 2
9 8 7 1

4 4
1231 1232 1233 1234
'''

import sys

N, M = map(int, sys.stdin.readline().split())

data = sorted(list(map(int, sys.stdin.readline().split())))

bucket = []

def select(k: int):

    if len(bucket) == M:
        print(*bucket)
        return

    for i in range(k, len(data)):
        bucket.append(data[i])
        select(i)
        bucket.pop()

select(0)
