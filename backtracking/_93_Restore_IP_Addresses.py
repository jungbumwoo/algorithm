class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        stack = []
        ans = []

        def select(s, i, n):
            if n == 5:
                if i == len(s):
                    ans.append(".".join(stack))
                return

            for k in range(1,4):
                if i + k > len(s):
                    continue

                str_num = s[i:i+k]
                int_num = int(str_num)

                if int_num > 255:
                    continue
                if len(str_num) != len(str(int_num)):
                    continue
                
                stack.append(str_num)
                select(s, i+k, n + 1)
                stack.pop()
        
        select(s, 0, 1)
        return ans
