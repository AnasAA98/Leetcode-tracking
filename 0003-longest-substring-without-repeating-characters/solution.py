class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subs = set()
        left = 0
        res = 0
        for ch in s:
            while ch in subs:
                subs.remove(s[left])
                left += 1
            subs.add(ch)
            res = max(res,len(subs))
        return res
            
