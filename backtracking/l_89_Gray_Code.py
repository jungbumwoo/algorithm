# fixme
# https://leetcode.com/problems/gray-code/


from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest

import sys
sys.setrecursionlimit(10 ** 8)

class Solution:
    def solve(self,  n: int) -> List[int]:
        if n == 1:
            return [0, 1]
        
        init_n = '0' * n
        init_dict = {}
        init_array = []
        ok, result = self.dfs(init_n, init_dict, init_array)

        ans = []
        for r in result:
            ans.append(int(r, 2))
        return ans

    def dfs(self, s: str, cache: dict, stack):
        if len(cache) == 2 ** len(s):
            return True, stack[:]

        if s in cache:
            return False, None

        for i in range(len(s)):
            if s[i] == '0':
                new = s[:i] + '1' + s[i+1:]
            else:
                new = s[:i] + '0' + s[i+1:]
    
            cache[s] = True
            stack.append(s)
            ok, result = self.dfs(new, cache, stack)

            if ok:
                return ok, result
            
            stack.pop()
            del cache[s]
        
        return False, None

# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            n: int

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(n = 1),
                expect=[0, 1],
            ),
            TestCase(
                name="test 2",
                input=Args(n = 2),
                expect=[0, 2, 3, 1],
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solve(n=c.input.n)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()