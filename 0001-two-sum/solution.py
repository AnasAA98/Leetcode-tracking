class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {} # key: nums , val: indx
        for i in range(len(nums)):
            k = target - nums [i]
            if k in map:
                return [i,map[k]]
            else:
                map[nums[i]] = i
        
