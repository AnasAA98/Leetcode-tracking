class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        # find the dup 
        # find the missing number
        n = len(nums) 
        res = [-1] * (n + 1)
        dup = -1
        for num in nums:
            if res[num] == -1:
                res[num] = num
            else:
                dup = num
        for i in range(1,n + 1):
            if res[i] == -1:
                return [dup,i]
