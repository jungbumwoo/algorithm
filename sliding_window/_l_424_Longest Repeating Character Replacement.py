from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# https://leetcode.com/problems/longest-repeating-character-replacement/

'''
You are given a string s and an integer k. 
You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.
'''

class Solution:
    def solve(self, s: str, k: int) -> List[int]:
        # Time Complexity :  
        # Space Complexity : 
        inital_window_size = k + 1 # 바꾸는 수 (k) + 최소 하나 (1)

        l, r = 0, 0 + inital_window_size - 1
        
        data = {}
        max_exists = 0
        for i in range(l, r + 1):
            if s[i] not in data:
                data[s[i]] = 1
            else:
                data[s[i]] += 1
            
            max_exists = max(data[s[i]], max_exists)
        
        window_size = k + max_exists
        search_end_point = len(s) - window_size

        def search(index, size, k):
            temp = {}
            max_exists = 0
            for t in range(size):
                point = index + t

                if point >= len(s):
                    return max_exists + k

                if s[point] not in temp:
                    temp[s[point]] = 1
                else:
                    temp[s[point]] += 1

                max_exists = max(max_exists, temp[s[point]])
            
            return max_exists + k


        for i in range(0, search_end_point):
            print(f"i: {i}, window_size: {window_size}")
            new_window_size = search(i, window_size, k)
            while new_window_size > window_size:
                window_size = new_window_size
                print(f"i: {i}, window_size: {window_size}")
                new_window_size = search(i, window_size, k)
                
        return window_size
    
        
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            s: str
            k: int

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(s = "AABABBA", k=1),
                expect=4
            ),
            TestCase(
                name="test 2",
                input=Args(s = "ABAB", k=2),
                expect=4
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solve(s=c.input.s, k=c.input.k)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
