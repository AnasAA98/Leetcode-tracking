class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        if s == t:
            return True
        counter_t = 0
        counter_s = 0
        while counter_s != len(s):
            if counter_t >= len(t):
                return False
            if s[counter_s] == t[counter_t]:
                counter_s+=1
            counter_t+=1
        return True
            
