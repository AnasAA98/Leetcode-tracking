class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        best = [0] * n
        best[0] = nums[0]
        best[1] = max(nums[0], nums[1])
        for i in range(2,n):
            best[i] = max(best[i-1],best[i-2]+nums[i])
        return best[-1]

