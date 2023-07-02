from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# https://leetcode.com/problems/decode-ways/
# solve cnt = 1
'''
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, 
all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways).

'''

import functools

class Solution:
    def solve(self, s: str) -> int:
        # Time Complexity :  
        # Space Complexity :     

        @functools.lru_cache(maxsize=None)
        def select(idx, cnt):
            if idx >= len(s) or idx + cnt > len(s):
               return 0

            total = 0
            if cnt == 2:
                v = int(s[idx:idx+2])
                if v > 26 or v < 10:
                    return 0
                
                if idx + 2 == len(s):
                    return 1
                
                total += select(idx+2, 1)
                total += select(idx+2, 2)
            
            if cnt == 1:
                if s[idx] == '0':
                    return 0
                
                if idx + 1 == len(s):
                    return 1

                total += select(idx+1, 1)
                total += select(idx+1, 2)

            return total
        
        return select(0, 1) + select(0, 2)

        
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass(frozen=True, slots=True, kw_only=True)
        class Args:
            s: str

        @dataclass(frozen=True, slots=True, kw_only=True)
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(s="12"),
                expect=2
            ),
            TestCase(
                name="test 2",
                input=Args(s="226"),
                expect=3
            ),
            TestCase(
                name="test 3",
                input=Args(s="06"),
                expect=0
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
