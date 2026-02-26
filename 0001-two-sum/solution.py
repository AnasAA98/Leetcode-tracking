class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        for i,n in enumerate(nums):
            diff = target - n
            if diff in my_map:
                return [my_map[diff], i]
            my_map[n] = i
            
        return None
