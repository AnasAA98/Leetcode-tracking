class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        res = 0
        lower = set()
        upper = set()
        for ch in word:
            if ch.islower():
                lower.add(ch)
            else:
                upper.add(ch)        
        for ch in upper:
            if ch.lower() in lower:
                res += 1
        return res
