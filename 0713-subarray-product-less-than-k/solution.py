class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1 or not nums:
            return 0
        result = 0
        curr_prod = 1
        left = 0
        for right in range(len(nums)):
            curr_prod*= nums[right]
            while curr_prod >= k:
                curr_prod = curr_prod // nums[left]
                left+=1
            result += right - left + 1
        return result
