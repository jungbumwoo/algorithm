# 아래 풀이는 왜 틀린걸까?

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        self.dx = [0,0,-1,1]
        self.dy = [-1,1,0,0]
        self.heights = heights
        self.visited = set()
        ans = []

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                pacific, atlantic = self.dfs(i, j)
                if pacific and atlantic:
                    ans.append([i, j])

        return ans

    @cache
    def dfs(self, row, col):
        init_row, init_col = False, False
        if row < 0 or col < 0:
            init_row = True

        if row >= len(self.heights) or col >= len(self.heights[0]):
            init_col = True

        if init_row or init_col:
            return init_row, init_col
        
        if (row, col) in self.visited:
            return False, False

        p, a = False, False
        
        nx, ny = row + self.dx[0], col + self.dy[0]
        if (nx < 0 or ny < 0) and (nx >= len(self.heights) or ny >= len(self.heights[0])):
            return True, True
        if nx < 0 or ny < 0:
            p = True
        if nx >= len(self.heights) or ny >= len(self.heights[0]):
            a = True
        if nx >= 0 and nx < len(self.heights) and ny >= 0 and ny < len(self.heights[0]):
            if self.heights[nx][ny] <= self.heights[row][col]:
                self.visited.add((row, col))
                p_0, a_0 = self.dfs(nx, ny)
                self.visited.remove((row, col))
                p = True if p_0 is True else p
                a = True if a_0 is True else a
                if p is True and a is True:
                    return p, a     

        nx, ny = row + self.dx[1], col + self.dy[1]
        if (nx < 0 or ny < 0) and (nx >= len(self.heights) or ny >= len(self.heights[0])):
            return True, True
        if nx < 0 or ny < 0:
            p = True
        if nx >= len(self.heights) or ny >= len(self.heights[0]):
            a = True
        if nx >= 0 and nx < len(self.heights) and ny >= 0 and ny < len(self.heights[0]):
            if self.heights[nx][ny] <= self.heights[row][col]:
                self.visited.add((row, col))
                p_1, a_1 = self.dfs(nx, ny)
                self.visited.remove((row, col))
                p = True if p_1 is True else p
                a = True if a_1 is True else a
                if p is True and a is True:
                    return p, a
        
        nx, ny = row + self.dx[2], col + self.dy[2]
        if (nx < 0 or ny < 0) and (nx >= len(self.heights) or ny >= len(self.heights[0])):
            return True, True
        if nx < 0 or ny < 0:
            p = True
        if nx >= len(self.heights) or ny >= len(self.heights[0]):
            a = True
        if nx >= 0 and nx < len(self.heights) and ny >= 0 and ny < len(self.heights[0]):
            if self.heights[nx][ny] <= self.heights[row][col]:
                self.visited.add((row, col))
                p_2, a_2 = self.dfs(nx, ny)
                self.visited.remove((row, col))
                p = True if p_2 is True else p
                a = True if a_2 is True else a
                if p is True and a is True:
                    return p, a

        nx, ny = row + self.dx[3], col + self.dy[3]
        if (nx < 0 or ny < 0) and (nx >= len(self.heights) or ny >= len(self.heights[0])):
            return True, True
        if nx < 0 or ny < 0:
            p = True
        if nx >= len(self.heights) or ny >= len(self.heights[0]):
            a = True
        if nx >= 0 and nx < len(self.heights) and ny >= 0 and ny < len(self.heights[0]):
            if self.heights[nx][ny] <= self.heights[row][col]:
                self.visited.add((row, col))
                p_3, a_3 = self.dfs(nx, ny)
                self.visited.remove((row, col))
                p = True if p_3 is True else p
                a = True if a_3 is True else a
                if p is True and a is True:
                    return p, a

        return p, a
