class Solution:
    def isUgly(self, n: int) -> bool:
        if n == 0:
            return False
        
        def divide(left: int, k: int):
            while True:
                if left % k != 0:
                    return left
                left //= k

        
        a = divide(n, 5)
        b = divide(a, 3)
        c = divide(b, 2)

        if c == 1:
            return True
        return False