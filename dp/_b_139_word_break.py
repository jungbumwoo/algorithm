import functools

from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# https://leetcode.com/problems/word-break

'''
description
'''

class Solution:
    def solve(self, s:str, wordDict: List[str]) -> bool:
        d = [False] * len(s)    
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
                    d[i] = True
        return d[-1]

        
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            s: str
            wordDict: List[str]

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(s="leetcode", wordDict=["leet","code"]),
                expect=True
            ),
            TestCase(
                name="test 2",
                input=Args(s="applepenapple", wordDict = ["apple","pen"]),
                expect=True
            ),
            TestCase(
                name="test 3",
                input=Args(s="catsandog", wordDict=["cats","dog","sand","and","cat"]),
                expect=False
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solve(s=c.input.s, wordDict=c.input.wordDict)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
