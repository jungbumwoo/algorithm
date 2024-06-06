# https://leetcode.com/problems/triangle

'''
cache를 class variable로 뒀더니 테스트 케이스간에 공유되는 문제가 있었다.
functools.cache로 해결하여 변경함

Bottom Up 으로 풀어볼 수도 있음.
'''

import functools

class Solution:

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.triangle = triangle
        return self.search(0, 0)

    @functools.cache
    def search(self, i, j):
        if i == len(self.triangle) or j == len(self.triangle) or j < 0:
            return 0

        return self.triangle[i][j] + min(self.search(i+1, j), self.search(i+1, j+1))
        