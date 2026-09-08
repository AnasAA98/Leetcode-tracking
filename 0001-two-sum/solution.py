class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i, num in enumerate(nums):
            cnd = target - num
            if cnd in seen:
                return [i, seen[cnd]]
            else:
                seen[num] = i
    

