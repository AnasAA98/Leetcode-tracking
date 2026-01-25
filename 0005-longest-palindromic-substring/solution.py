class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l-=1
                r+=1
            return l+1,r-1
        best_l,best_r = 0,0
        for i in range(len(s)):
            l1,r1 = check(i,i) # case of an odd palindrome
            l2,r2 = check(i,i+1) # case of an even palindrome

            if best_r - best_l < r1-l1:
                best_l,best_r = l1,r1
            if best_r - best_l < r2-l2:
                best_l,best_r = l2,r2
        return s[best_l:best_r+1]


