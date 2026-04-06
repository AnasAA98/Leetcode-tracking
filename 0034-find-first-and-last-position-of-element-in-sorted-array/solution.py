class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bns (isLeft):
            left = 0
            right = len(nums) - 1
            temp = -1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    temp = mid
                    if isLeft:
                        right = mid-1
                    else:
                        left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return temp
        left = bns(True)
        right = bns(False)
        return [left,right]







