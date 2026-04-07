# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0,0
            left_h,left_diam = dfs(node.left)
            right_h, right_diam = dfs(node.right)
            height = 1 + max(left_h,right_h)
            diam = max(left_diam,right_diam,left_h+right_h)
            return height,diam
        return dfs(root)[1]

