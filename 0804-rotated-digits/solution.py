class Solution:
    def rotatedDigits(self, n: int) -> int:
        def isGood(x):
            diff = False
            while x > 0:
                d = x % 10
                if d in {3, 4, 7}:
                    return False
                if d in {2,5,6,9}:
                    diff = True
                x = x // 10
            return diff
        res = 0
        for i in range(n + 1):
            if isGood(i):
                res+=1
        return res
