# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        q.append(root)
        last_level= [root]
        node_parent = {root:None}
        while q:
            last_level = []
            for _ in range(len(q)):
                curr = q.popleft()
                last_level.append(curr)
                if curr.left:
                    q.append(curr.left)
                    node_parent[curr.left] = curr
                if curr.right:
                    q.append(curr.right)
                    node_parent[curr.right] = curr
        res = set(last_level)
        while len(res) > 1:
            res = {node_parent[node] for node in res}
        return  next(iter(res))

