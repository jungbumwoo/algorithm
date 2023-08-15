from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest

# https://leetcode.com/problems/ones-and-zeroes


class Solution:
    def solve1(self, strs: List[str], m: int, n: int) -> List[int]:
        # fixme
        cache = {}
        def dfs(i, m, n):
            if i == len(strs):
                return 0

            if (i, m, n) in cache:
                return cache[(i, m, n)]

            cache[(i, m, n)] = dfs(i+1, m, n)
            zeros, ones = strs[i].count('0', 0, len(strs[i]) - 1), strs[i].count('1', 0, len(strs[i]) - 1)
            if m - zeros >= 0 and n - ones >= 0:
                cache[(i, m, n)] = max(dfs(i+1, m - zeros, n - ones) + 1, cache[(i, m, n)])

            return cache[(i, m, n)]

        return dfs(0, m, n)

        
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            strs: List[str]
            m: int
            n: int


        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(strs=["10","0001","111001","1","0"], m=5, n=3),
                expect=4
            ),
            TestCase(
                name="test 2",
                input=Args(strs=["10","0","1"], m=1, n=1),
                expect=2
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solve1(strs=c.input.strs, m=c.input.m, n=c.input.n)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
