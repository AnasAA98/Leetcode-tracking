# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0,0
            left_sum,left_tilt = dfs(node.left)
            right_sum,right_tilt = dfs(node.right)
            tilt = abs(left_sum - right_sum)
            tilt+= left_tilt+ right_tilt
            return left_sum+right_sum+node.val, tilt
        return dfs(root)[1]     

