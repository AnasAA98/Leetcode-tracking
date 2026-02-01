# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0,0,0  # sum elements + number elements + counter
            left_sum, left_size, left_count = dfs(node.left)
            right_sum, right_size, right_count = dfs(node.right)
            s = left_sum + right_sum + node.val
            size = right_size + left_size + 1
            count = left_count + right_count 
            if s // size == node.val:
                count+=1
            return s + node.val,size+1, count
        return dfs(root)[2]
