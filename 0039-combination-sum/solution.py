class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def dfs(start,rem,path):
            if rem == 0:
                res.append(path[:])
                return
            for i in range(start,len(candidates)):
                num = candidates[i]
                if num > rem:
                    break
                path.append(num)
                dfs(i,rem - num,path)
                path.pop()
            
        dfs(0,target,[])
        return res
