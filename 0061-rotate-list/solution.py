# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        size = 0
        curr = head
        while curr:
            size+=1
            curr = curr.next
        k = k % size
        if k == 0:
            return head
        curr = head
        for _ in range(size-k-1):
            curr=curr.next
        temp = curr.next
        curr.next = None
        result = temp
        while temp.next:
            temp = temp.next
        temp.next = head
        return result  

