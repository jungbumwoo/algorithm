from collections import defaultdict

class Solution:

    # 처음 풀이
    def findLHS(self, nums: List[int]) -> int:

        data = defaultdict(int)

        for num in nums:
            data[num] += 1

        before = - (10 ** 9)
        ans = 0

        for key in sorted(data.keys()):

            if key - before == 1:
                if data[key] + data[before] >= ans:
                    ans = data[key] + data[before]
            before = key

        return ans
    
    # 시간복잡도 개선
    def findLHS_2(self, nums: List[int]) -> int:

        data = defaultdict(int)

        for num in nums:
            data[num] += 1

        ans = 0

        for key in data.keys():
            if key + 1 in data:
                ans = max(data[key] + data[key+1], ans)

        return ans
