class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        map = {}
        for ch in magazine:
            map[ch] = map.get(ch,0)+1
        for ch in ransomNote:
            if ch not in map or map[ch]<=0:
                return False
            else:
                map[ch]-=1
        return True

