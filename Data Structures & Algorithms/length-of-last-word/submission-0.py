class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        result = s.split()
        last_word = result[-1]
        return len(last_word)