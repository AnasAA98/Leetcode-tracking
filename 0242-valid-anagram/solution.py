class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        my_map = defaultdict(int)
        for c in s:
            my_map[c] += 1
        for c in t:
            if c in my_map:
                my_map[c] -= 1
            else:
                return False
        for k in my_map:
            if my_map[k] != 0:
                return False
        return True
        
        
