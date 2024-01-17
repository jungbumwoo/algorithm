# https://www.acmicpc.net/problem/20057

import sys

N = int(sys.stdin.readline())

data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(data)

# west, south, east, north
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0] 

def is_thrown_out(n, m):
    if n < 0 or n >= N or m < 0 or m >= N:
        return True
    return False

def split(board, p, q, direction_index):

    amout_of_thrown_out = 0

    # 5%
    # five_moved = five_split()
    five_precent_sands = (board[p][q] * 5) // 100
    x_five_spot, y_five_spot = p + 2 * dx[direction_index], q + 2 * dy[direction_index]

    if is_thrown_out(x_five_spot, y_five_spot):
        amout_of_thrown_out += five_precent_sands
    else:
        data[x_five_spot][y_five_spot] += five_precent_sands

    # 10%
    # ten_moved = ten_split()

    # 7%
    # seven_moved = seven_split()

    # 2%
    # two_moved = two_split()

    # how to handle 75% sand? should I subtract form above? or jush multiply 0.75?


def main():

    pivots = set()
    start_x, start_y = N // 2, N // 2
    direction_index = 0
    pivots.add((start_x, start_y))

    # move
    nx, ny = start_x + dx[direction_index], start_y + dy[direction_index]

    # split
    data, nx, ny, direction_index


    # move


    # wind

