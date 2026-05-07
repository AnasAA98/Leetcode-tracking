class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        # step 1 gravity logic
        for row in boxGrid:
            empty = n - 1
            for j in range(n - 1, -1, -1):
                if row[j] =="*":
                    empty = j - 1
                elif row[j] == "#":
                    row[j], row[empty] = row[empty],row[j]
                    empty -= 1
        # step 2 rotation
        result =[['.'] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                result[j][m - i -1] = boxGrid[i][j]
        return result

