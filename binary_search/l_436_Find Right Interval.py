from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# Link

'''
description
'''

class Solution:
    def solve(self, intervals: List[List[int]]) -> List[int]:
        # Time Complexity :  
        # Space Complexity : 
        if len(intervals) == 1:
            return [-1]
        data = []
        for i in range(len(intervals)):
            data.append([intervals[i][0], intervals[i][1], i])
        data.sort()
        ans = []

        for j in range(len(intervals)):
            target = intervals[j][1]
            start, end = 0, len(data) - 1
            res_idx = len(data)
            while start <= end:
                mid = (start + end) // 2
                if data[mid][0] >= target:
                    end = mid - 1
                else:
                    start = mid + 1
            
            if res_idx == len(data):
                ans.append(-1)
            else:
                ans.append(data[res_idx][2])
        return ans

        
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            intervals: List[List[int]]

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(intervals = [[1,2]]),
                expect=[-1]
            ),
            TestCase(
                name="test 2",
                input=Args(intervals = [[3,4],[2,3],[1,2]]),
                expect=[-1, 0, 1]
            ),
            TestCase(
                name="test 3",
                input=Args(intervals = [[1,4],[2,3],[3,4]]),
                expect=[-1, 2, -1]
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solve(intervals=c.input.intervals)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
