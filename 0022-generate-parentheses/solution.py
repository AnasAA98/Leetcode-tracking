class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(num_open,num_close,path):
            if num_open == n and n == num_close:
                res.append("".join(path))
                return
            if num_open < n:
                path.append("(")
                dfs(num_open+1,num_close,path)
                path.pop()
            if num_close < num_open :
                path.append(")")
                dfs(num_open,num_close+1,path)
                path.pop()
        dfs(0,0,[])
        return res
