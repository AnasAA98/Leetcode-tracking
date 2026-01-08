class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        n = len(s)
        for i in range(n):
            if s[i] != "]":
                stack.append(s[i])
            else:
                sub = ""
                while stack[-1] != "[":
                    sub = stack.pop() + sub
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k)*sub)
        return "".join(stack)
