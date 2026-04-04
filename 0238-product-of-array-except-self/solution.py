class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        prefx = 1
        for i in range(n):
            res[i] = prefx
            prefx *= nums[i]
        sufx = 1
        for i in range(n-1,-1,-1):
            res[i] *= sufx
            sufx *= nums[i]
        return res
