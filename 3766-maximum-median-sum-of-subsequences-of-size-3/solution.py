class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums)-1
        result = 0
        while left <= right:
            result+=nums[right-1]
            left+=1
            right-=2
        
        return result
