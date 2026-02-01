class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        skip = set() # set of indices to remove
        stack = [] # keep track of valid parenthese 
        for i,ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            if ch == ')':
                if stack:
                    stack.pop()
                else:
                    skip.add(i)
        for index in stack:
            skip.add(index)
        res = []
        for i,ch in enumerate(s):
            if i in skip:
                continue
            else:
                res.append(ch)
        return "".join(res)
