# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        def count_paths(node,curr):
            if not node:
                return 0
            curr += node.val
            count = 1 if curr == targetSum else 0
            return count + count_paths(node.left,curr) + count_paths(node.right,curr)
        def dfs(node):
            if not node:
                return 0
            return count_paths(node,0) + dfs(node.left) + dfs(node.right)
        
        return dfs(root)
