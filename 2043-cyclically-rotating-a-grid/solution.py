class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0] * n for _ in range(m)]
        number_layers = min(m, n) // 2
        for i in range(number_layers):
            ring = []
            top    =  i
            bottom = m - 1 - i
            left   = i
            right  = n - 1 - i
            for j in range(top,bottom + 1):
                ring.append(grid[j][left])
            for j in range(left + 1, right + 1):
                ring.append(grid[bottom][j])
            for j in range(bottom - 1, top - 1, -1):
                ring.append(grid[j][right])
            for j in range(right -1,left,-1):
                ring.append(grid[top][j])
            l = len(ring)
            k_eff = k % l
            ring = ring[-k_eff:]+ ring[:-k_eff]
            indx = 0
            for p in range(top, bottom +1):
                res[p][left] = ring[indx]
                indx += 1
            for p in range(left + 1, right + 1):
                res[bottom][p] = ring[indx]
                indx += 1
            for p in range(bottom - 1, top - 1, -1):
                res[p][right] = ring[indx]
                indx +=1
            for p in range(right -1,left,-1):
                res[top][p] = ring[indx]
                indx += 1
        return res



