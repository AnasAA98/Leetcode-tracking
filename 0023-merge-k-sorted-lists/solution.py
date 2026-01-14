# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        my_list = []
        for n_list in lists:
            curr = n_list
            while curr:
                my_list.append(curr.val)
                curr = curr.next
        my_list.sort()
        head = ListNode(0)
        curr = head
        for num in my_list:
            curr.next = ListNode(num)
            curr = curr.next
        return head.next
