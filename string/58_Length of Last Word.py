class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        flag = True
        count = 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == " " and flag:
                continue
            elif s[i] == " ":
                return count
            else:
                flag = False
                count += 1
        
        return count