# each value we push will be in a form of a tuple 
# each tuple will contain the value and the minimum element so far in the stack
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        
        min_element = self.stack[-1][1] if self.stack and self.stack[-1][1] < val else val
        self.stack.append((val,min_element))
    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]
    def getMin(self) -> int:
        return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
