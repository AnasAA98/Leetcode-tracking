class Solution:
    def integerReplacement(self, n: int) -> int:
        nums = {1:0}
        def dfs(i):
            if i in nums:
                return nums[i]
            if i % 2 == 0:
                nums[i] = 1 + dfs(i//2)
            else:
                nums[i] = 1 +  min(dfs(i+1),dfs(i-1))
            return nums[i]
        return dfs(n)
