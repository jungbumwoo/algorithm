import heapq
from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# https://leetcode.com/problems/maximum-length-of-pair-chain

'''
description
'''

class Solution:
    def solve(self, pairs: List[List[int]]) -> int:

        queue = list()
        heapq.heapify(queue)

        for i in range(len(pairs)):
            s, e = pairs[i]
            heapq.heappush(queue, [e, s])
        
        last_num, cnt = -100000, 0
        while queue:
            end, start = heapq.heappop(queue)

            if start > last_num:
                cnt += 1
                last_num = end

        return cnt
        
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            pairs: List[int]

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(pairs = [[1,2],[2,3],[3,4]]),
                expect=2
            ),
            TestCase(
                name="test 2",
                input=Args(pairs = [[1,2],[7,8],[4,5]]),
                expect=3
            ),
            TestCase(
                name="test 3",
                input=Args(pairs = [[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10],[-4,7]]),
                expect=4
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solve(pairs=c.input.pairs)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()



