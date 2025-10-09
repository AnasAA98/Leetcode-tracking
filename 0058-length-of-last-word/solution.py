class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        word = list(s)
        counter= 0
        i = -1
        while i >= -len(word) and word[i] != " ":
            counter += 1
            i -= 1
        return counter

