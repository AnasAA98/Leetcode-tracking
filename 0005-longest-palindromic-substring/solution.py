class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        def check (l, r):
            while l >=0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1
        l_res, r_res = 0, 0
        for i in range(n):
            # odd palindrome:
            left, right = check(i, i + 1)
            if right - left > r_res - l_res:
                l_res, r_res = left, right
            
            # even palindrome
            left,right = check(i,i)
            if right - left > r_res - l_res:
                l_res, r_res = left, right
        return s[l_res: r_res + 1]
            
            

