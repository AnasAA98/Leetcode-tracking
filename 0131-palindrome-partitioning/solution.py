class Solution:
    def partition(self, s: str) -> List[List[str]]:
        path = []
        result = []
        n = len(s)
        def dfs(i):
            if i == n:
                result.append(path[:])
                return
            for j in range(i, n):
                x = s[i:j+1]
                if x == x[::-1]:
                    path.append(x)
                    dfs(j+1)
                    path.pop()
        dfs(0)
        return result
