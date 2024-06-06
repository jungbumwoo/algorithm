# https://leetcode.com/problems/triangle

class Solution:
    cache = {}

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.triangle = triangle
        return self.search(0, 0)

    
    def search(self, i, j):
        if i == len(self.triangle) or j == len(self.triangle) or j < 0:
            return 0

        if (i, j) in self.cache:
            return self.cache[(i, j)]
        
        ans = self.triangle[i][j] + min(self.search(i+1, j), self.search(i+1, j+1))
        self.cache[(i, j)] = ans
        return ans
