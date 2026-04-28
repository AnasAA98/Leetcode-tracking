class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        flat = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                flat.append(grid[i][j])
        flat.sort()
        steps = 0
        n = len(flat)
        median = flat[n//2]
        for val in flat:
            if val % x != flat[0] % x:
                return -1
            steps += abs(val - median) // x
        return steps
