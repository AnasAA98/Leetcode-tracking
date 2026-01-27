class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []
        path = []
        n = len(s)
        def dfs(index,):
            if len(path) == 4:
                if index == n:
                    result.append(".".join(path))
                return
            for i in range(1,4):
                if index+i > n:
                    continue
                seg=s[index:index+i]
                if i > 1 and seg[0] == "0":
                    continue
                if int(seg) > 255:
                    continue
                path.append(seg)
                dfs(index+i)
                path.pop()
        dfs(0)
        return result
