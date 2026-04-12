class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        left = 0
        right = n - 1
        def check(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        while left < right:
            if s[left] != s[right]:
                return check(left,right-1) or check(left+1,right)
            left+=1
            right-=1
        return True
