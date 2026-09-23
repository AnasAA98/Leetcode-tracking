class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seq = set()
        res = 0
        left = 0
        for c in s:
            while c in seq:
                seq.remove(s[left])
                left += 1
            seq.add(c)
            res = max(res, len(seq))
        return res
