class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        counter = 0
        word = list(s)
        i = len(word) - 1
        while word[i] != ' ' and i >= 0:
            counter+=1
            i-=1
        return counter
