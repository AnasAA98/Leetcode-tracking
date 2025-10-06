class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}  # value -> index
        for i, n in enumerate(nums):
            dif = target - n
            if dif in mp:
                return [mp[dif], i]
            mp[n] = i


