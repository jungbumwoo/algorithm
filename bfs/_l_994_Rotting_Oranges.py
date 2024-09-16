from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ans = 0
        queue = deque()
        total_cnt, rotten_cnt = 0, 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                    rotten_cnt += 1
                if grid[i][j] != 0:
                    total_cnt += 1

        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]

        while queue:
            p, q, day = queue.popleft()
            ans = day

            for k in range(4):
                nx, ny = p + dx[k], q + dy[k]

                if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
                    continue

                if grid[nx][ny] != 1:
                    continue

                grid[nx][ny] = 2
                rotten_cnt += 1
                queue.append((nx, ny, day + 1))
        
        if total_cnt != rotten_cnt:
            return -1

        return ans
