from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# https://leetcode.com/problems/letter-case-permutation

'''
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.
'''

class Solution:
    def solve(self, s: str) -> List[str]:
        data = []
        output = []

        def dfs(i):
            if i == len(s):
                joined = ''.join(data)
                output.append(joined)
                return

            if s[i].isalpha() is False:
                data.append(s[i])
                dfs(i+1)
                data.pop()
            else:
                data.append(s[i].upper())
                dfs(i+1)
                data.pop()

                data.append(s[i].lower())
                dfs(i+1)
                data.pop()
        dfs(0)
        return output


        
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            s: str

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(s = "a1b2"),
                expect=['A1B2', 'A1b2', 'a1B2', 'a1b2']
            ),
            TestCase(
                name="test 2",
                input=Args(s = "3z4"),
                expect=['3Z4', '3z4']
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solve(s=c.input.s)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
