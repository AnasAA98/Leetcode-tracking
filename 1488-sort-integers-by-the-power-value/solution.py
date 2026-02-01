class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        cache = {1:0}

        result = []
        def power(x):
            if x in cache:
                return cache[x]
            nxt = x // 2 if x % 2 == 0 else 3 * x + 1
            cache[x] = 1 + power(nxt)
            return cache[x]
        for i in range(lo,hi+1):
            result.append((power(i),i))
        result.sort()
        return result[k-1][1]
