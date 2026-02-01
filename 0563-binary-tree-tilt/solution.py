# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def dfs(node):  # dfs will return sum + current tilt
            if not node :
                return 0,0
            left_node,left_tilt = dfs(node.left)
            right_node,right_tilt = dfs(node.right)
            tilt = abs(left_node - right_node) + left_tilt + right_tilt
            return left_node+right_node + node.val,tilt
        return dfs(root)[1]
