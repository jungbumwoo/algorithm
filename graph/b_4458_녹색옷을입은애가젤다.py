import heapq
import sys

INF = 10 ** 7
dx = (1, 0, -1, 0)
dy = (0, -1, 0, 1)

'''
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
0
'''

def dijkstra(data: list):
    start = (0, 0)
    history = [[INF] * len(data) for _ in range(len(data))]
    start_cost = data[0][0]
    history[0][0] = start_cost
    q = []
    heapq.heapify(q)
    heapq.heappush(q, (start_cost, start))

    while q:
        curr_cost, curr_position  = heapq.heappop(q)
        curr_x, curr_y = curr_position

        if curr_cost > history[curr_x][curr_y]:
            continue
        
        for i in range(4):
            new_x = curr_x + dx[i]
            new_y = curr_y + dy[i]

            if new_x < 0 or new_x >= len(data) or new_y < 0 or new_y >= len(data):
                continue
            distance = curr_cost + data[new_x][new_y]

            if distance < history[new_x][new_y]:
                history[new_x][new_y] = distance
                heapq.heappush(q, (distance, (new_x, new_y)))

    return history[-1][-1]

k = 1
while True:
    N = int(sys.stdin.readline())
    if N == 0: break

    data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    result = dijkstra(data)
    print(f'Problem {k}: {result}')
    k += 1