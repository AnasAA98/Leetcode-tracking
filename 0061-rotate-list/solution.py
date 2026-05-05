# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        l = 0
        curr = head
        while curr:
            l +=1
            curr = curr.next
        k = k % l
        dummy = ListNode(0)
        prev = dummy
        curr = head
        n = 0
        while n != l - k - 1:
            curr = curr.next
            n += 1
        nxt = curr.next
        curr.next = None
        curr = nxt
        while curr:
            prev.next = curr
            curr = curr.next
            prev = prev.next
        prev.next = head
        return dummy.next
