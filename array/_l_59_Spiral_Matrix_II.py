class Solution:
    direction = 0
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    def get_next_direction(self):
        self.direction = (self.direction + 1) % 4
        return self.direction

    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0] * n for _ in range(n)]

        x, y = 0, 0
        N = n*n
        for i in range(1, N + 1):
            result[x][y] = i

            nx = x + self.dx[self.direction]
            ny = y + self.dy[self.direction]

            if nx < 0 or nx >= n or ny < 0 or ny >= n or result[nx][ny] > 0:
                new_direction = self.get_next_direction()
                nx, ny = x + self.dx[new_direction], y + self.dy[new_direction]
            
            x, y = nx, ny

        return result

    