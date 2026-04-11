class Solution:
    def addDigits(self, num: int) -> int:
        if num <= 9 :
            return num
        res = 0
        while num > 0:
            res+= num % 10
            num = num // 10
        if res > 9:
            return self.addDigits(res)
        return res

