class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 2
        for right in range(2,len(nums)):
            if nums[left - 2] != nums[right]:
                nums[left],nums[right] = nums[right],nums[left]
                left +=1
        return left

