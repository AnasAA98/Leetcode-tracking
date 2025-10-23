class Solution:
    def hasSameDigits(self, s: str) -> bool:
        result = [int(ch) for ch in s]
        print(result)
        while len(result) >2:
            temp = []
            for i in range(len(result)-1):
                a = result[i]
                b=result[i+1]
                c = a+b
                temp.append(c%10)
            result = temp
        return result[0] == result[1]
