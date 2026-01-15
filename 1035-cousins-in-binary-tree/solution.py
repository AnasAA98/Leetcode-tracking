# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        q = deque()
        q.append(root)
        while q:
            found_x,found_y = False,False
            for _ in range(len(q)):
                curr = q.popleft()
                if curr.left and curr.right:
                    a,b = curr.left.val, curr.right.val
                    if (a==x and b ==y) or(a==y and b==x):
                        return False
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                if curr.val == x:
                    found_x = True
                if curr.val == y:
                    found_y = True
            if found_x and found_y:
                return True
            if found_x or found_y:
                return False
        return False
