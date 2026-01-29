class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        path = []
        def dfs(num_open,num_close):
            if num_close == n and num_open==n:
                result.append("".join(path))
            if num_open < n:
                path.append('(')
                dfs(num_open+1, num_close)
                path.pop()
            if num_close < num_open:
                path.append(')')
                dfs(num_open, num_close+1)
                path.pop()
        dfs(0,0)
        return result
