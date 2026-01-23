class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                substring = ""
                while stack[-1] != "[":
                    ch = stack.pop()
                    substring = ch + substring
                stack.pop()
                mult = ""
                while stack and stack[-1].isdigit():
                    ch = stack.pop()
                    mult =  ch+ mult 
                stack.append(int(mult) * substring)
        return "".join(stack)
