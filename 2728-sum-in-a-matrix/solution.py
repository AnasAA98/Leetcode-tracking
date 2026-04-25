class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        m,n = len(nums), len(nums[0])
        sorted_nums = [sorted(row, reverse = True) for row in nums]
        res = 0
        for j in range(n):
            curr_max = 0
            for i in range(m):
                curr_max = max(curr_max,sorted_nums[i][j])
            res += curr_max
        return res
