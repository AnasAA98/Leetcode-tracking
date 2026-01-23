"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        adj = defaultdict(list)
        seen = set()
        def build_adj_list(node):
            q=deque()
            q.append(node)
            seen.add(node)
            while q:
                curr_node = q.popleft()
                adj[curr_node]
                for nei in curr_node.neighbors:
                    adj[curr_node].append(nei)
                    if nei not in seen:
                        seen.add(nei)
                        q.append(nei)
        build_adj_list(node)
        copy_dict ={}
        for orig in adj:
            copy_dict[orig] = Node(orig.val)
        for orig,nei in adj.items():
            copy_node = copy_dict[orig]
            for n in nei:
                copy_node.neighbors.append(copy_dict[n])
        return copy_dict[node]

