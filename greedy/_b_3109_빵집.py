import sys

'''
input)
5 5
.xx..
..x..
.....
...x.
...x.

ans)
2


input)
6 10
..x.......
.....x....
.x....x...
...x...xx.
..........
....x.....

ans)
5
'''

R, C = map(int, sys.stdin.readline().split())

data = [list(*sys.stdin.readline().rsplit()) for _ in range(R)]
visited = [[-1] * C for _ in range(R)]
connected = [-1] * R
result = 0

def right_above(i, n, m):
    if n < 0 or m >= C:
        return False
    
    if data[n][m] == 'x' or visited[n][m] >= 0:
        return False
    return True

def right(i, p, q):
    if q >= C:
        return False
    if data[p][q] == 'x' or visited[p][q] >= 0:
        return False
    return True

def right_below(i, n, m):
    if n >= R or m >= C:
        return False
    if data[n][m] == 'x' or visited[n][m] >= 0:
        return False
    return True

def find(i, p, q):
    global result

    if connected[i] == i: # already connected
        return

    if q == C -1: # arrived
        result += 1
        connected[i] = i
        return

    if right_above(i, p-1, q+1) and connected[i] != i:
        visited[p-1][q+1] = i
        find(i, p-1, q+1)

        if connected[i] != i:
            visited[p-1][q+1] = -1

    if right(i, p, q+1) and connected[i] != i:
        visited[p][q+1] = i
        find(i, p, q+1)

        if connected[i] != i:
            visited[p][q+1] = -1

    if right_below(i, p+1, q+1) and connected[i] != i:
        visited[p+1][q+1] = i
        find(i, p+1, q+1)

        if connected[i] != i:
            visited[p+1][q+1] = -1

def search(i):
    find(i, i, 0)
    return

for i in range(R):
    search(i)

print(result)