class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        first_list = s1.split(" ")
        second_list = s2.split(" ")

        first_phase, second_phase = set(), set()

        for word in first_list:
            self.handle_word(first_phase, second_phase, word)
        for word in second_list:
            self.handle_word(first_phase, second_phase, word)
        return list(first_phase)
        
    @staticmethod
    def handle_word(first_phase, second_phase, word):
        if word in second_phase:
            return