# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # helper function that i will use to revert each chunk of my linked list
        def helper(node, end):
            prev_node = None
            curr_node = node
            while curr_node != end:
                temp = curr_node.next
                curr_node.next = prev_node
                prev_node = curr_node
                curr_node = temp 
            return prev_node
        curr = head
        length = 0
        # get length of the linked list
        while curr:
            length +=1
            curr = curr.next
        # get number of chunks 
        chunks = length // k
        # iterate for every chunk reverse the nodes in it and link it to previous chunks 
        dummy = ListNode(0,head) 
        prev = dummy
        for _ in range(chunks): # itterate over number of chunks
            chunk_start = prev.next # store a pointer to chunk start
            chunk_end = chunk_start # move chunk end until i reach end of the chunk
            for _ in range(k-1): # k-1 since i already start at the node itself
                chunk_end = chunk_end.next #keep moving until i reach end of chunk
            next_chunk = chunk_end.next # store pointer to next chunk
            prev.next = helper(chunk_start,next_chunk) # reverse the chunk using help function
            chunk_start.next = next_chunk # start a new chunk 
            prev = chunk_start # update prev pointer
        return dummy.next
