class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        array = s.split()
        res = []

        for w in array:
            try:
                res.append(int(w))
            except ValueError:
                continue
        
        for i in range(1,len(res)):
            if res[i] <= res[i - 1]:
                return False
        return True
            

