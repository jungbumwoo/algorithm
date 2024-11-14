# space complexity O(1) 으로 풀어볼 것 

class Solution:
    def reverseWords(self, s: str) -> str:
        
        stack = []
        temp = ""
        for i in range(len(s)):
            if s[i] == " ":
                if temp != "":
                    stack.append(temp)
                    temp = ""
            else:
                temp += s[i]
        if temp != "":
            stack.append(temp)
        
        ans = ''
        for j in range(len(stack)-1, -1, -1):
            ans += stack[j] + ' '
        
        return ans[:-1]