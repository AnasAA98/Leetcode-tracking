class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        l, r = 0, n - 1

        def check (l,r):
            while l>=0 and r < n and s[l] == s[r]: # withing boundaries and we can expand left and right 
                l -= 1
                r += 1
            return l+1, r-1
        left, right = 0,0
        for i in range(n):
            l1,r1 = check(i,i) # odd pal
            l2,r2 = check(i,i+1) # even pal
            
            if right - left < r1 - l1:
                left,right = l1,r1
            if right - left < r2 - l2:
                left,right = l2,r2
        return s[left:right+1]
