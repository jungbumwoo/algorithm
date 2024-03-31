class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:

        ascii_target = ord(target)
        ascii_max = ord('z')

        is_not_exist = True
        for letter in letters:
            if ord(letter) > ascii_target and ord(letter) < ascii_max:
                ascii_max = ord(letter)
                is_not_exist = False
        
        if is_not_exist:
            return letters[0]
        
        return chr(ascii_max)
