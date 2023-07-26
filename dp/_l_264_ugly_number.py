# fixme # Timeout

class Solution:
    candidates = [2, 3, 5]
    data = set()

    def nthUglyNumber(self, n: int) -> int:

        if n == 1:
            return 1

        self.data.add(1)

        flag = 2
        cnt = 1
        while True:

            if self.is_valid(flag):
                self.data.add(flag)
                cnt += 1
            
            if cnt == n:
                return flag
            
            flag += 1

    def is_valid(self, num):

        for candi in self.candidates:
            left = num % candi
            share = num // candi

            if left == 0 and share in self.data:
                return True

        return False

