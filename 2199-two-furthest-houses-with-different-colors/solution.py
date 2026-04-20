class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        res = 0
        for i in range(n):
            if colors[i] != colors[n -1]:
                res = max(res, abs(n-1-i))
                break
        for j in range(n-1,-1,-1):
            if colors[j] != colors[0]:
                res = max(res,abs(j))
                break
        return res
