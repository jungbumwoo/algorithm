from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# https://leetcode.com/problems/number-of-islands/description/

'''
description
'''
from collections import deque 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                queue = deque()
                if grid[i][j] == "1":
                    cnt += 1
                    queue.append((i, j))

                while queue:
                    x, y = queue.popleft()
                    grid[x][y] = "0"
                    for i in range(4):
                        nx, ny = x + dx[i], y + dy[i]   

                        if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
                            continue
                        if grid[nx][ny] == "0":
                            continue

                        queue.append((nx, ny))
        
        return cnt



        
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            nums: List[int]

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(nums = [-4,-1,0,3,10]),
                expect=[0,1,9,16,100]
            ),
            TestCase(
                name="test 2",
                input=Args(nums = [-7,-3,2,3,11]),
                expect=[4,9,9,49,121]
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solve(nums=c.input.nums)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
