# https://leetcode.com/problems/word-pattern/


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        p = list(pattern)
        q = list(s.split(' '))

        if len(p) != len(q):
            return False

        data = {}
        for c, word in zip(p, q):
            if c in data:
                if word != data[c]:
                    return False
            else:
                data[c] = word

        duplicate = {}
        for _, v in data.items():
            if v in duplicate:
                return False
            else:
                duplicate[v] = True

        return True