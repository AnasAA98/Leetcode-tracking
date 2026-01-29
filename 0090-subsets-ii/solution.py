class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        path = []
        result = set()
        n = len(nums)
        def dfs(index):
            if index == n:
                result.add(tuple(path))
                return
            dfs(index+1)
            path.append(nums[index])
            dfs(index+1)
            path.pop()
        dfs(0)
        return [list(t) for t in result]            

