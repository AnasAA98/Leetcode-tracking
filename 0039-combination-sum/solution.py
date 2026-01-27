class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        path = []
        n = len(candidates)
        def dfs(start,rem):
            # if my rem is == 0 means i have a valid comb sum
            if rem == 0:
                result.append(path[:])
                return
            for i in range(start,n):
                num = candidates[i]
                if num > rem:
                    break
                path.append(candidates[i])
                dfs(i,rem-num)
                path.pop()
        
        dfs(0,target)
        return result 
