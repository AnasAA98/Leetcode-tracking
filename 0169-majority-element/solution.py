class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        freq = 0
        for x in nums:
            if freq == 0:
                candidate = x
                freq = 1
            elif x == candidate:
                freq += 1
            else :
                freq -= 1
        return candidate 
