class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check length
        if len(s) != len(t):
            return False
        my_map = defaultdict(int)
        for ch in s:
            my_map[ch] +=1
        for c in t:
            if c not in my_map or my_map[c] == 0:
                return False
            else:
                my_map[c] -= 1
        return True
        
