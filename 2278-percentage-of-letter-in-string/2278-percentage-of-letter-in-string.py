class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        p = s.count(letter)
        return int((p/len(s) )*100)
        