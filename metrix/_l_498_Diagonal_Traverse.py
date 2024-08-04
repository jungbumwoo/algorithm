from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest

# https://leetcode.com/problems/diagonal-traverse/

'''
'''

class Solution:
    def solve(self, mat: List[List[int]]) -> List[int]:
        result = []
        self.last_x, self.last_y = -1, 0
        while True:
            self.last_x, self.last_y, r = self.ascend(self.last_x, self.last_y, mat)
            if len(r) == 0:
                return result

            for x in r:
                result.append(x)
            
            self.last_x, self.last_y, r = self.descend(self.last_x, self.last_y, mat)
            if len(r) == 0:
                return result

            for x in r:
                result.append(x)


    def ascend(self, x:int, y:int, mat: List[List[int]]):
        result = []
        if x + 1 >= len(mat) and y + 1 >= len(mat[0]):
            return None, None, result

        if x+1 < len(mat):
            new_x, new_y = x+1, y
        elif y + 1 < len(mat[0]):
            new_x, new_y = x, y + 1
        else:
            raise ValueError('unexpected case')

        last_x, last_y = new_x, new_y
        while new_x >= 0 and new_y < len(mat[0]):
            result.append(mat[new_x][new_y])
            last_x, last_y = new_x, new_y
            new_x, new_y = new_x - 1, new_y + 1
            
        return last_x, last_y, result

    def descend(self, x:int, y:int, mat: List[List[int]]):
        result = []
        if x + 1 >= len(mat) and y + 1 >= len(mat[0]):
            return None, None, result
        
        if y + 1 < len(mat[0]):
            new_x, new_y = x, y + 1
        elif x + 1 < len(mat):
            new_x, new_y = x + 1, y
        else:
            raise ValueError(f'unexpected case: {x}, {y}')
        
        last_x, last_y = new_x, new_y
        while new_x < len(mat) and new_y >= 0:
            result.append(mat[new_x][new_y])
            last_x, last_y = new_x, new_y
            new_x, new_y = new_x + 1, new_y - 1
        
        return last_x, last_y, result



# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            mat: List[List[int]]

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(mat = [[1,2,3],[4,5,6],[7,8,9]]),
                expect=[1,2,4,7,5,3,6,8,9],
            ),
            TestCase(
                name="test 2",
                input=Args(mat = [[1,2],[3,4]]),
                expect=[1,2,3,4],
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solve(mat=c.input.mat)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
