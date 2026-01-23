# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1,s2 = [],[]
        curr = l1
        while curr:
            s1.append(curr.val)
            curr = curr.next
        curr = l2
        while curr:
            s2.append(curr.val)
            curr = curr.next
        carry = 0
        head = None
        while s1 or s2 or carry:
            x = s1.pop() if s1 else 0
            y = s2.pop() if s2 else 0
            total = x + y + carry
            carry = total // 10
            node = ListNode(total % 10)
            node.next = head
            head = node
        return head
            
        
