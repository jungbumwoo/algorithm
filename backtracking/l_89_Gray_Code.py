# fixme
# https://leetcode.com/problems/gray-code/

import sys
sys.setrecursionlimit(10 ** 8)

class Solution:
    def grayCode(self, n: int) -> List[int]:

        if n == 1:
            return [0, 1]
        
        init_n = '0' * n
        init_dict = {}
        init_array = []
        ok, result = self.dfs(init_n, init_dict, init_array)

        ans = []
        for r in result:
            ans.append(int(r, 2))
        return ans

    def dfs(self, s: str, cache: dict, stack):
        if len(cache) == 2 ** len(s) - 1:
            return True, stack[:]

        if s in cache:
            return False, None

        for i in range(len(s)):
            if s[i] == '0':
                new = s[:i] + '1' + s[i+1:]
            else:
                new = s[:i] + '0' + s[i+1:]
    
            cache[s] = True
            stack.append(s)
            ok, result = self.dfs(new, cache, stack)

            if ok:
                return ok, result
            
            stack.pop()
            del cache[new]
        
        return False, None
