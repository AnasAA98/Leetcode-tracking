# LeetCode format
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        steps = length - n
        prev = dummy

        for _ in range(steps):
            prev = prev.next
        prev.next = prev.next.next

        return dummy.next

