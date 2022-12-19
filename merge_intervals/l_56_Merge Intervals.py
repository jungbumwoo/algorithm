from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# https://leetcode.com/problems/merge-intervals/

'''
Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
'''

class Solution:
    def solve(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        data = [[-1, -1]]
        for interval in intervals:
            start, end = interval[0], interval[1]

            if start <= data[-1][1]:
                data[-1][1] = max(data[-1][1], end)
            else:
                data.append([start, end])

        return data[1:]

        
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
                input=Args(intervals = [[1,3],[2,6],[8,10],[15,18]]),
                expect=[[1,6],[8,10],[15,18]]
            ),
            TestCase(
                name="test 2",
                input=Args(intervals = [[1,4],[4,5]]),
                expect=[[1,5]]
            ),
            TestCase(
                name="test 3",
                input=Args(intervals = [[1,4],[2,3]]),
                expect=[[1,4]]
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
