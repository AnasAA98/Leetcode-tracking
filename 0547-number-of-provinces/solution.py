class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = set()
        res = 0
        def explore(i):
            visited.add(i)
            for j in range(n):
                if isConnected[i][j] ==1 and j not in visited:
                    explore(j)
        for i in range(n):
            if i not in visited:
                res+=1
                explore(i)
        return res
