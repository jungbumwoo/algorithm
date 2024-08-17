# https://leetcode.com/problems/max-number-of-k-sum-pairs/description
# fixme: RuntimeError: dictionary changed size during iteration

from collections import defaultdict

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        data = defaultdict(int)
        
        for n in nums:
            data[n] += 1

        for _key, v in data.items():
            target = k - _key

            if target == _key:
                ans += (v // 2) 
            else:
                min_value = min(data[target], v)
                ans += min_value
                data[target] -= min_value
                data[_key] -= min_value

        return ans