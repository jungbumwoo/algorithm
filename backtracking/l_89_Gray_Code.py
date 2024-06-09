# fixme
# https://leetcode.com/problems/gray-code/

class Solution:
    def grayCode(self, n: int) -> List[int]:
        
        init_n = '0' * n
        init_dict = {}
        init_dict[init_n] = True
        init_array = []
        init_array.append(init_n)
        ok, result = self.dfs(init_n, {}, [])
        print(f'ok: {ok}, result: {result}')

        ans = []
        for r in result:
            ans.append(int(r, 2))
        return ans

    def dfs(self, s: str, cache: dict, stack):

        # if len full -> return success
        # in s in cache: -> 

        if len(cache) == 2 ** len(s) - 1:
            return True, stack[:]

        if s in cache:
            return False, None

        for i in range(len(s)):
            if s[i] == '0':
                new = s[:i] + '1' + s[i+1:]
            else:
                new = s[:i] + '0' + s[i+1:]
            
            cache[new] = True
            stack.append(new)
            ok, result = self.dfs(new, cache, stack)

            if ok:
                return ok, result
            
            stack.pop()
            del cache[new]
        
        return False, None
