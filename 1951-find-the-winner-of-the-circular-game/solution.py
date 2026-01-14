class Node:
    def __init__(self, val = 0, next =0):
        self.val = val
        self.next = next
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        head = Node()
        tail = head
        for i in range(1,n+1):
                tail.next = Node(i)
                tail = tail.next
        tail.next = head.next
        curr = head.next
        prev = tail 
        while n>1:
            counter = 1
            while counter != k:
                prev = curr 
                curr = curr.next
                counter+=1
            prev.next = curr.next
            curr = curr.next
            n-=1
        return curr.val
                









            
