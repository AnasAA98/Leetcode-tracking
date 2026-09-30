class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        res = 0
        curr = x
        while curr != 0:
            res = (res * 10) + curr % 10
            curr = curr // 10
        return x == res

