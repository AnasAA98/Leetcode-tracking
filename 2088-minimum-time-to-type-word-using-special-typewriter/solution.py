class Solution:
    def minTimeToType(self, word: str) -> int:
        ans = 0
        pos = 0

        for ch in word:
            nxt = ord(ch) - ord('a')
            diff = abs(nxt - pos)
            ans+= min(diff,26-diff) + 1
            pos = nxt
        return ans
