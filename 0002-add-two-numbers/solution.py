# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""
        curr1 = l1
        curr2 = l2
        while curr1:
            num1 += str(curr1.val)
            curr1 = curr1.next
        while curr2:
            num2 += str(curr2.val)
            curr2 = curr2.next
        result = int(num1[::-1]) + int(num2[::-1])
        result = str(result)
        print(result)
        output = ListNode(0)
        curr = output

        for i in range(len(result) - 1, -1, -1):
            curr.next = ListNode(int(result[i]))
            curr = curr.next
        return output.next

