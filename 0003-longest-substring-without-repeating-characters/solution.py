class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set ()
        left = 0
        res = 0
        for i in range(len(s)):
            if s[i] in seen:
                while s[i] in seen:
                    seen.remove(s[left])
                    left+=1
            seen.add(s[i])
            res = max(res, i - left + 1)
        return res
