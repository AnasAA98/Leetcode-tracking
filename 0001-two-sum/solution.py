class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,num in enumerate(nums):
            cand = target - num
            if cand in seen:
                return[i,seen[cand]] 
            seen[num] = i
