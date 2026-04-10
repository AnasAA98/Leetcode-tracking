class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                curr = nums[i] + nums[left] + nums[right]
                if abs(curr - target) < abs(res - target):
                    res = curr
                if curr == target:
                    return res
                elif curr < target:
                    left +=1
                else:
                    right -= 1
        return res
