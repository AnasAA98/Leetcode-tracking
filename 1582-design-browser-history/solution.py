class ListNode:
    def __init__(self, val = 0, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(homepage)
        self.curr = self.head
    def visit(self, url: str) -> None:
        node = ListNode(url)
        self.curr.next = node
        node.prev = self.curr
        self.curr = self.curr.next
    def back(self, steps: int) -> str:
        curr_pos = self.curr
        while curr_pos.prev and steps>0:
            curr_pos = curr_pos.prev
            steps-=1
        self.curr = curr_pos
        return curr_pos.val
    def forward(self, steps: int) -> str:
        curr_pos = self.curr
        while curr_pos.next and steps>0:
            curr_pos = curr_pos.next
            steps-=1
        self.curr = curr_pos
        return curr_pos.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
