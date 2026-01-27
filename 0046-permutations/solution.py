class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        n = len(nums)
        def dfs(path):
            if len(path) == n:
                result.append(path[:])
                return
            for x in nums:
                if x not in path:
                    path.append(x)
                    dfs(path)
                    path.pop()        
        dfs(path)
        return result
