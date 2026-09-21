class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left  = 0
        right = len(nums) - 1

        while left < right :
            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]: # the peak is on the right of nums[mid]
                left = mid + 1
            else:
                right = mid
        return right
