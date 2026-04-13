class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        seen = set()
        def dfs(key):
            if key in seen:
                return
            seen.add(key)
            for room in rooms[key]:
                dfs(room)
        dfs(0)
        return len(seen) == len(rooms)
