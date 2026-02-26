class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        res = 0
        left = 0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left+=1
            seen.add(s[i])
            res = max(res,len(seen))
        return res
