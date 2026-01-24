# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0 
        curr = head
        while curr:
            n+=1
            curr = curr.next
        n = n //2
        curr = head
        while n !=0:
            n-=1
            curr = curr.next
        return curr
