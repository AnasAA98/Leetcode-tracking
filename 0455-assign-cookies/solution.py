class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        j = 0
        count = 0
        for i in range(len(g)):
            while j < len(s) and s[j] < g[i]:
                j += 1
            if j == len(s):
                break
            count+=1
            j+=1
        return count
