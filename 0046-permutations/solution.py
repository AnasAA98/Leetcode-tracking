class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        n = len(nums)
        def dfs(index):
            if index == n:
                result.append(path[:])
                return
            for x in nums:
                if x not in path:
                    path.append(x)
                    dfs(index+1)
                    path.pop()        

        dfs(0)
        return result
