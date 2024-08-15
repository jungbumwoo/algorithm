# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length
# 다시 풀기

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        data = [[0, 0] for _ in range(len(s))]
        vowels = set(list('aeiou'))
        if s[0] in vowels:
            data[0][0] = 1
            data[0][1] = 1
            
        ans = data[0][0]
        
        for i in range(1, len(s)):
            data[i][0] = data[i-1][1] + (1 if s[i] in vowels else 0)
            ans = max(ans, data[i][0])
            if i - (k - 1) < 0:
                data[i][1] = data[i][0]
            elif s[i - (k - 1)] in vowels:
                data[i][1] = data[i][0] - 1
            else:
                data[i][1] = data[i][0]
        print(data)
        return ans