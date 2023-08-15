from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest

# https://leetcode.com/problems/ones-and-zeroes

'''
오답노트
a = 'aaaaa'

# range [ )
print(a.count('a')) # 5
print(a.count('a', 0, len(a))) # 5
print(a.count('a', 0, len(a) -1)) # 4

print(a.count('aa')) # 2
'''

class Solution:
    def solve1(self, strs: List[str], m: int, n: int) -> List[int]:
        # Top Down
        cache = {}
        def dfs(i, m, n):
            if i == len(strs):
                return 0

            if (i, m, n) in cache:
                return cache[(i, m, n)]

            cache[(i, m, n)] = dfs(i+1, m, n)
            zeros, ones = strs[i].count('0', 0, len(strs[i])), strs[i].count('1', 0, len(strs[i]))
            if m - zeros >= 0 and n - ones >= 0:
                cache[(i, m, n)] = max(dfs(i+1, m - zeros, n - ones) + 1, cache[(i, m, n)])

            return cache[(i, m, n)]

        return dfs(0, m, n)

    def solve2(self, strs: List[str], m: int, n: int) -> List[int]:

        '''
        Bottom-up
        
        3차원 배열 쓰는거나, defaultdict 활용하는걸 알게됨.
        '''

        from collections import defaultdict

        cache = defaultdict(int)

        for i in range(len(strs)):
            s = strs[i]
            for M in range(m + 1):
                for N in range(n + 1):

                    zeros, ones = s.count('0'), s.count('1')

                    if M - zeros >= 0 and N - ones >= 0:
                        cache[(i, M, N)] = max(
                            cache[(i-1, M - zeros, N - ones)] + 1,
                            cache[(i-1, M, N)]
                        )
                    else:
                        cache[(i, M, N)] = cache[(i-1, M, N)]

        return cache[(len(strs)-1, m, n)]

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
            actual = solution.solve2(strs=c.input.strs, m=c.input.m, n=c.input.n)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
