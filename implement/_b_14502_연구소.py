# https://www.acmicpc.net/problem/14502
# 연구소

import sys
from itertools import combinations
'''
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

27

------------
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2

9

------------
8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0

3
'''

M, N = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

print(f"initial data: {data}")

empty = []
virous = []

for i in range(M):
    for j in range(N):
        if data[i][j] == 0:
            empty.append((i, j))

        elif data[i][j] == 2:
            virous.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def mark(board, x, y):

    if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
        return 0
    
    if board[x][y] != 0:
        return 0
    
    ans = 1
    board[x][y] = 2

    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        ans += mark(board, nx, ny)

    return ans


def play(board, virous):
    ans = 0

    for i in range(len(virous)):
        x, y = virous[i][0], virous[i][1]
        
        for j in range(4):
            nx, ny = x + dx[j], y + dy[j]
            ans += mark(board, nx, ny)
    return ans

initial_count = play(data[:], virous)
answer = 0
for combi in combinations([t for t in range(len(empty))], 3):

    for c in combi:
        board = data[:]
        board[empty[c][0]][empty[c][1]] = 1

        new_game_count = play(board, virous)
        diff = initial_count - new_game_count

        answer = max(new_game_count, answer)

print(answer)
