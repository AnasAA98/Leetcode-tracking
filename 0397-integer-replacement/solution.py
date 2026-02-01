class Solution:
    def integerReplacement(self, n: int) -> int:
        nums = {1:0}
        def dfs(d):
            if d in nums:
                return nums[d]
            if d % 2 == 0:
                nums[d] = 1 + dfs(d // 2)
            else:
                nums[d] = 1 + min(dfs(d-1),dfs(d+1))
            return nums[d]
        dfs(n)
        return nums[n]
