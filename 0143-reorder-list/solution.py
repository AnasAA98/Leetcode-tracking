# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr = head
        stack = []
        while curr:
            stack.append(curr)
            curr = curr.next
        n = len(stack)
        start = (n + 1) // 2
        stack[start - 1].next = None
        stack = stack[start:] 
        curr = head
        while stack:
            nxt = curr.next
            node = stack.pop()
            curr.next = node
            node.next = nxt
            curr = nxt
        

