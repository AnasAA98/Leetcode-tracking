class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if not num1:
            return num2
        if not num2:
            return num1
        n = len(num1)-1
        m = len(num2)-1
        carry = 0
        result = []
        while n >=0 or m>=0:
            x1 = int(num1[n]) if n>=0 else 0
            x2 = int(num2[m]) if m >= 0 else 0
            val = x1 + x2 + carry 
            carry = val // 10
            val = val % 10
            result.append(str(val))
            n -=1
            m-=1
        if carry:
            result.append(str(carry))
        return "".join(result[::-1])
