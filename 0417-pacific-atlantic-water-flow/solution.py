class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        # intersection of both paci and atl
        pac = set()
        atl = set()
        def explore(r,c,seen,prev):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in seen or heights[r][c] < prev:
                return
            seen.add((r,c))
            explore(r - 1, c, seen, heights[r][c])
            explore(r + 1, c, seen, heights[r][c])
            explore(r, c - 1, seen, heights[r][c])
            explore(r, c + 1, seen, heights[r][c])
        for i in range(rows):
            explore(i,0,pac,heights[i][0])
            explore(i,cols-1,atl,heights[i][cols - 1])
        for j in range(cols):
            explore(0,j,pac,heights[0][j])
            explore(rows -1,j,atl,heights[rows -1 ][j])
        return [(r,c) for r,c in (pac & atl)]
