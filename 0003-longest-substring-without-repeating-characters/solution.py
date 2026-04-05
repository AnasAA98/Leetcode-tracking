class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_length = 0
        left = 0        
        for i in range(len(s)):
            if s[i] in seen:
                while s[i] in seen:
                    seen.discard(s[left])
                    left+=1
            seen.add(s[i])
            max_length = max(max_length,i- left+1)
        return max_length

