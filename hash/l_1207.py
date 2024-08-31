from collections import defaultdict

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        d = defaultdict(int)
        for num in arr:
            d[num] += 1

        s = set()

        for _, value in d.items():
            if value in s:
                return False
            s.add(value)
        
        return True