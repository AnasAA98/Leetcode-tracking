# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        def reverse(node,k):
            prev = None
            curr = node
            while k > 0:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                k -=1
            return prev,node,curr
        prev = None
        curr = head
        pos = 1
        while pos < left:
            prev = curr
            curr = curr.next
            pos+=1
        k = (right - left) + 1
        new_head,new_tail,next_node = reverse(curr,k)
        if prev:
            prev.next = new_head
        else:
            head = new_head
        new_tail.next = next_node
        return head
        
            
