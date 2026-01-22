# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        level = 0
        max_sum = (root.val,1)
        while q:
            curr_sum = 0
            for _ in range(len(q)):
                curr = q.popleft()
                curr_sum += curr.val
                if curr.left :
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            level+=1
            x,y = max_sum
            if curr_sum > x:
                max_sum = (curr_sum,level)
        return max_sum[1]
