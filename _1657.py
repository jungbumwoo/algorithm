# https://leetcode.com/problems/determine-if-two-strings-are-close

# fixme
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        
        set_a = set(c for c in word1)
        set_b = set(c for c in word2)

        if len(set_a) != len(set_b):
            return False

        return True