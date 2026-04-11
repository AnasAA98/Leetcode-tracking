class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s1 = 0
        for ch in s:
            s1+= ord(ch)
        t1 = 0
        for ch in t:
            t1 += ord(ch)
        return chr(t1-s1)

