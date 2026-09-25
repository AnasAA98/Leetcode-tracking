class Solution:
    def countPairs(self, n: int, edges: list[list[int]]) -> int:

        # build adjacency list
        adj = defaultdict(list)
        visited = set()
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        def dfs(node:int) -> int:
            # takes input a node returns # of nodes reachable from set node
            if node in visited:
                return 0
            visited.add(node)
            curr = 1
            for nei in adj[node]:
                curr += dfs(nei)
            
            return curr
        res = 0
        for node in range(n):
            if node in visited:
                continue
            curr_size = dfs(node)
            res += curr_size * (n - curr_size)

        return res //2


            
