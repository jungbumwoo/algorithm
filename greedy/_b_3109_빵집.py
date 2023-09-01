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

# fix: 이미 실패했던 경로라면 다시 visit 할 필요가 없다. 성공했다면 visit 불가능. pypy 통과
# fix: python 도 통과. 재귀함수 중간에 return 되는 구조로 변경함

R, C = map(int, sys.stdin.readline().split())

data = [list(*sys.stdin.readline().rsplit()) for _ in range(R)]
visited = [[-1] * C for _ in range(R)]
result = 0

d = [(-1, 1), (0, 1), (1, 1)]

def find(i, p, q):
    global result

    if q == C -1: # arrived
        result += 1
        return True
    
    for direction in d:
        new_x = p + direction[0]
        new_y = q + direction[1]

        if new_x < 0 or new_y < 0 or new_x >= R or new_y >= C:
            continue

        if visited[new_x][new_y] >= 0:
            continue

        if data[new_x][new_y] == 'x':
            continue
        
        visited[new_x][new_y] = i
        if find(i, new_x, new_y) is True:
            return True


for i in range(R):
    find(i, i, 0)

print(result)