class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_ch = 0
        l = 0 
        seen = set()
        for r,ch in enumerate(s):
            while ch in seen:
                seen.remove(s[l])
                l+=1
            seen.add(ch)
            max_ch = max(max_ch,r-l + 1)
        return max_ch
