class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ind = {}
        for i,val in enumerate(nums):
            target_val = target - val
            if target_val in dict_ind:
                return [i,dict_ind[target_val]]
            dict_ind[val] = i
