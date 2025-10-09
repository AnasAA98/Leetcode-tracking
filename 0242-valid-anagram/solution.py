class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map = {}
        for ch in s:
            map[ch] = map.get(ch, 0) + 1
        for ch in t:
            map[ch] = map.get(ch, 0) - 1
        for key in map:
            if map[key] != 0:
                return False
        return True

