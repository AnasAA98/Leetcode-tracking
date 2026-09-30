class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0 :
            sign = -1
            x = abs(x)
        if x > 2**(32):
            return 0
        res = 0
        while x != 0:
            res = res * 10 + (x % 10) 
            x = x // 10
        if res > (2**31) - 1:
            return 0
        res *= sign
        return res 

