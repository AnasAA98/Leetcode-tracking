# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count = 0
        def dfs(node):
            nonlocal count
            if not node:
                return 0,0
            left_sum,left_count = dfs(node.left)
            right_sum,right_count = dfs(node.right)
            s = left_sum + right_sum + node.val
            c = left_count+ right_count+1
            if s//c == node.val:
                count+=1
            return s,c
        dfs(root)
        return count

