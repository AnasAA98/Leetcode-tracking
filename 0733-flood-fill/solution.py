class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row, col = len(image), len(image[0])
        ori = image[sr][sc]
        def dfs(r,c):
            if r < 0 or r >= row or c < 0 or c >= col or image[r][c] == color or image[r][c] != ori  :
                return
            image[r][c] = color
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        dfs(sr,sc)
        return image
