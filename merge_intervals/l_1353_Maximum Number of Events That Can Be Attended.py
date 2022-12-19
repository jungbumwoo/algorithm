from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

'''
You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.
You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.
Return the maximum number of events you can attend.
'''

class Solution:
    def solve(self, events: List[List[int]]) -> int:
        # Time Complexity :  
        # Space Complexity : 
        raise NotImplementedError

        
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            events: List[int]

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(events = [[1,2],[2,3],[3,4]]),
                expect=3
            ),
            TestCase(
                name="test 2",
                input=Args(events= [[1,2],[2,3],[3,4],[1,2]]),
                expect=4
            ),
            TestCase(
                name="test 3",
                input=Args(events= [[1,2],[1,2],[3,3],[1,5],[1,5]]),
                expect=5
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solve(nums=c.input.events)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
