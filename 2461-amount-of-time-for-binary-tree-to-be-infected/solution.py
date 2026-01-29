# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # key constraint need to find the node that is infected
        # need to keep track of parent of each node as well
        map_parent = {root:None} # node.child:node
        infected_node = None
        q = deque()
        q.append(root)
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.val == start:
                    infected_node = curr
                if curr.left:
                    map_parent[curr.left] = curr
                    q.append(curr.left)
                if curr.right:
                    map_parent[curr.right] = curr
                    q.append(curr.right)
        q.append(infected_node)
        mins = -1
        visited_node = set()
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                visited_node.add(curr)
                for nxt in (curr.left,curr.right,map_parent[curr]):
                    if nxt and nxt not in visited_node:
                        q.append(nxt)
            mins+=1
        return mins

