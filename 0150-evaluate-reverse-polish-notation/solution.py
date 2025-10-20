class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opp= "+-/*"
        for ch in tokens:
            if ch in opp:
                a = stack.pop()
                b = stack.pop()
              
                if ch == "+":
                    stack.append(a+b)
                elif ch == '*':
                    stack.append(a*b)
                elif ch =='-':
                    stack.append(b-a)
              
                else:
                    stack.append(int(b/a))
            
            else:
                stack.append(int(ch))
        return stack[0]
