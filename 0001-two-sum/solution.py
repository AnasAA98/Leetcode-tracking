class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i,num in enumerate(nums):
            compl = target - num
            if compl in seen:
                return [i, seen[compl]]
            seen[num] = i
        
