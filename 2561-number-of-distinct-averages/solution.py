class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums) - 1
        res = set()
        while left < right :
            avg = (nums[left] + nums[right]) / 2
            res.add(avg)
            left += 1
            right -= 1
        return len(res)

