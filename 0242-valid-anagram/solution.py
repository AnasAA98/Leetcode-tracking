class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        res = defaultdict(int)
        for ch in s:
            res[ch] += 1
        for ch in t:
            if ch not in res or res[ch] == 0:
                return False
            res[ch] -= 1
        return True

