class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        # find the dup 
        # find the missing number
        n = len(nums)
        res = [False] * (n + 1)

        dup = -1
        for num in nums:
            if res[num] == True:
                dup = num
            res[num] = True
        
        for i in range(1,len(res)):
            if not res[i]:
                return [dup,i]

