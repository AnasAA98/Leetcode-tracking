class Solution:
    def isValid(self, s: str) -> bool:
        mapping ={")":"(", "]":"[","}":"{"}
        stack = []
        for ch in s:
            if ch in mapping.values():
                stack.append(ch)
            else:
                if not stack:
                    return False
                elif stack[-1]!= mapping[ch]:
                    return False
                else:
                    stack.pop()
        return not stack
