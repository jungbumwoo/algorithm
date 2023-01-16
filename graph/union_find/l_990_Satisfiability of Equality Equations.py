from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# https://leetcode.com/problems/satisfiability-of-equality-equations/

'''
You are given an array of strings equations that represent relationships between variables where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".
xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.
'''

class Solution:
    def solve(self, equations: List[str]) -> bool:
        # Time Complexity :  O(n)
        # Space Complexity : O(n)
        equations.sort(key=lambda x: x[1], reverse=True)
        data = {}

        def find(k):
            if data[k] == k:
                return k
            return find(data[k])

        def union(a, b):
            a_parent = find(a)
            b_parent = find(b)
            if a_parent < b_parent:
                data[b] = a_parent
                data[b_parent] = a_parent
            else:
                data[a] = b_parent
                data[a_parent] = b_parent

        for sentence in equations:
            p = ord(sentence[0])
            q = ord(sentence[3])
            if p not in data:
                data[p] = p
            if q not in data:
                data[q] = q

            if sentence[1] == "=":
                union(p, q)
            else:
                if find(p) == find(q):
                    return False
        return True
                
                

        
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            equations: List[str]

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: bool

        cases = [
            TestCase(
                name="test 1",
                input=Args(equations = ["a==b","b!=a"]),
                expect=False
            ),
            TestCase(
                name="test 2",
                input=Args(equations = ["b==a","a==b"]),
                expect=True
            ),
            TestCase(
                name="test 3",
                input=Args(equations = ["b!=f","c!=e","f==f","d==f","b==f","a==f"]),
                expect=False
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solve(equations=c.input.equations)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
