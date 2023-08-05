from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# https://leetcode.com/problems/edit-distance/


class Solution:
    def solve(self, word1: str, word2: str) -> List[int]:
        if len(word1) == 0 or len(word2) == 0:
            return max(len(word1), len(word2))

        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        for i in range(len(word1) + 1):
            for j in range(len(word2) + 1):
                if i == 0:
                    dp[i][j] = j
                
                if j == 0:
                    dp[i][j] = i

                if word1[i-1] == word2[j-1]:
                    dp[i][j] = min(dp[i-1][j-1], dp[i-1][j] + 1, dp[i][j-1] + 1)
                else:
                    dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1)
        return dp[-1][-1]


        
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            word1: str
            word2: str

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(word1 = "horse", word2 = "ros"),
                expect=3
            ),
            TestCase(
                name="test 2",
                input=Args(word1 = "intention", word2 = "execution"),
                expect=5
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solve(word1=c.input.word1, word2=c.input.word2)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()

