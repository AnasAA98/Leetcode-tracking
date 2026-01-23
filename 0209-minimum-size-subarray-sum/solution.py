class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        result = inf #MINIMUM SIZE ARRAY TO RETUN
        curr_sum = 0
        for right in range(len(nums)):
            curr_sum+=nums[right]
            while curr_sum>=target:
                result =min(result,right-left+1)
                curr_sum-=nums[left]
                left+=1
             
        return 0 if result== inf else result


