class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        def seperate(n):
            st = str(num)
            for ch in st:
                res.append(int(ch))
        for num in nums:
            seperate(num)
        return res

