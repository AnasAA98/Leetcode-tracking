class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 or x == 0:
            return x
        left = 1
        right = x
        res = 1
        while left <= right:
            mid = (left+right) // 2
            if mid * mid <= x:
                res = mid
                left = mid + 1
            else:
                right = mid -1 
        return res
