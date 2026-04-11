class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        left = 0
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
                count +=1
        return count

