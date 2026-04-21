class Solution:
    def mirrorDistance(self, n: int) -> int:
        x = n
        result = 0
        while x != 0:
            result = result * 10 + x % 10
            x //= 10
        return abs(n - result)
         
