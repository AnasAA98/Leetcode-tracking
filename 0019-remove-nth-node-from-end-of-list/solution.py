# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr. next
        if n == size:
            return head.next
        c = 1
        curr = head
        while curr and c != size - n:
            curr = curr.next
            c+=1
        if curr.next.next:
            curr.next = curr.next.next
        else:
            curr.next = None
        return head
        

