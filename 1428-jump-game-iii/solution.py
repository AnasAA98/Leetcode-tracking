class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        seen = set()
        def dfs(index):
            if index < 0 or index>= len(arr):
                return False
            if arr[index] == 0:
                return True
            if index in seen:
                return False
            seen.add(index)
            return dfs(index + arr[index]) or dfs(index - arr[index])

        return dfs(start)
