class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = nums[0] # represnts current max index that i can reach
        for i in range(1,len(nums)):
            if i <= max_reach: 
                # meaning my max_reach can reach i at any point
                max_reach = max(max_reach,i + nums[i]) # if i can reach i then i reach i + nums[i]
                # we use max beacuse what if the current max is already large enough to reach end so
                # no need to update
            else:
                return False
        return True
