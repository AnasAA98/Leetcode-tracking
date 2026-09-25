class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def check(l,r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r -1 
        left, right = 0, 0
        for i in range(n):
            l1,r1 = check(i,i)
            l2,r2 = check(i,i+1)
            if right - left < r1 - l1:
                right,left = r1, l1
            if right - left < r2 - l2:
                right, left = r2, l2
        return s[left:right + 1]

