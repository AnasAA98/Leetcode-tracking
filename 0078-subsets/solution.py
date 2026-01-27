class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []
        n = len(nums)
        def dfs(index):
            if index == n:
                result.append(path[:])
                return
            dfs(index+1)
            path.append(nums[index])
            dfs(index+1)
            path.pop()

        dfs(0)
        return result
