from dataclasses import dataclass
from typing import List, Optional, Tuple
import unittest


# https://leetcode.com/problems/super-ugly-number

'''
A super ugly number is a positive integer whose prime factors are in the array primes.
Given an integer n and an array of integers primes, return the nth super ugly number.
The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
'''

class Solution:
    def solve(self, n, primes):
        size = len(primes)
        ugly = 1
        dp = [1] 
        index = [0] * size
        ugly_nums = [1] * size
        print(f'primes: {primes}')

        for i in range(1, n):
            # compute possibly ugly numbers and update index
            print(f'ugly_nums: {ugly_nums}, ugly: {ugly}')
            print(f'dp: {dp}')

            for j in range(0, size):
                if ugly_nums[j] == ugly:
                    ugly_nums[j] = dp[index[j]] * primes[j]
                    index[j] += 1
            # get the minimum
            ugly = min(ugly_nums)
            dp.append(ugly)
            print("----------------")
            
        return dp[-1]

    def solve1(self, n: int, primes: List[int]) -> int:
        # Time Complexity :  
        # Space Complexity : 
        if n == 1:
            return 1
        uglys = [1]
				# 중복체크을 위해서 존재
        uglys_set = set([1])
        idxes = [0 for _ in range(len(primes))]
        while len(uglys) < n:
            print(f'uglys: {uglys}')
            candidates = []
						# ugly number 후보와, 어떤 prime 을 썻는지을 저장.
            for i, (prime, idx) in enumerate(zip(primes, idxes)):
                print(f'i: {i}, (prime, idx): {(prime, idx)}')
                print(f'uglys[idx]: {uglys[idx]}, prime: {prime}')
                candidates.append((uglys[idx]* prime, i))
            print(candidates)
            
            cur = min(candidates)
            idxes[cur[1]] += 1
						# 중복된 숫자가 잇다면 무시. 예를 들어 2*7, 7*2 같은 경우
            if cur[0] in uglys_set:
                continue
            uglys_set.add(cur[0])
            uglys.append(cur[0])
            print(f'idxes: {idxes}')
            print('================================')
            
        return uglys[-1]

        
# Test
class TestSolution(unittest.TestCase):
    def test_solution(self):
        @dataclass
        class Args:
            n: int
            primes: List[int]

        @dataclass
        class TestCase:
            name: str
            input: Args
            expect: int

        cases = [
            TestCase(
                name="test 1",
                input=Args(n = 12, primes = [2,7,13,19]),
                expect=32
            ),
            TestCase(
                name="test 2",
                input=Args(n = 1, primes = [2,3,5]),
                expect=1
            ),
        ]

        solution = Solution()
        for c in cases:
            actual = solution.solve(n=c.input.n, primes=c.input.primes)

            self.assertEqual(
                c.expect,
                actual,
                f"failed test {c.name} expected {c.expect}, actual {actual}"
            )


if __name__ == '__main__':
    unittest.main()
