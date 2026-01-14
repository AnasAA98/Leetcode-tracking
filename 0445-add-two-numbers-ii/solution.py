# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        curr = l1
        while curr:
            num1 = num1*10 + curr.val
            curr = curr.next
        num2 = 0
        curr = l2
        while curr:
            num2 = num2 * 10 + curr.val
            curr = curr.next
        total = num1+ num2
        head = ListNode(0)
        curr = head
        for ch in (str(total)):
            new_node = ListNode(int(ch))
            curr.next = new_node
            curr = curr.next
        return head.next



