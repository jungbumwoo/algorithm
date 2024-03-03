# loop 안쓰고 풀어보기
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False

        left, right = 0, 31

        while left <= right:
            mid = (left + right) // 2
            power_of_four = 4 ** mid
            if power_of_four == n:
                return True
            elif power_of_four < n:
                left = mid + 1
            else:
                right = mid -1
        
        return False
        