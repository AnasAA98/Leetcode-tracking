class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(open,close,path):
            if open == close == n:
                res.append("".join(path))
                return
            if open < n:
                path.append("(")
                backtrack(open + 1, close, path)
                path.pop()
            if close < open:
                path.append(")")
                backtrack(open,close + 1, path)
                path.pop()
        backtrack(0,0,[])
        return res


