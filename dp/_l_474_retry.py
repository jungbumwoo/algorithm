class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cache = {}
        def select(i, m, n):
            if i == len(strs):
                return 0
            if (i, m, n) in cache:
                return cache[(i, m, n)]
            
            m_count = m - strs[i].count("1")
            n_count = n - strs[i].count("0")
            a, b = 0, 0
            if m_count >= 0 and n_count >= 0:
                a = select(i+1, m_count, n_count) + 1
            b = select(i+1, m, n)
            ans = max(a, b)
            cache[(i, m, n)] = ans
            return ans

        a = select(0, m, n)
        print(cache)
        return a
            