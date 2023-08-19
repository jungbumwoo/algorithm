# https://leetcode.com/problems/reverse-vowels-of-a-string

class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        v = []
        index = []
        words = []
        

        for i in range(len(s)):
            if s[i] in vowels:
                index.append(i)
                v.append(s[i])
                
            words.append(s[i])

        l, r = 0, len(index) - 1

        while l < r:
            words[index[l]], words[index[r]] = v[r], v[l]
            l += 1
            r -= 1

        return ''.join(words)
