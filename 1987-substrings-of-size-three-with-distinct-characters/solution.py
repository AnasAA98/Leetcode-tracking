class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        k = 3
        n = len(s)
        if n < k:
            return 0
        window = len(set(s[:k]))
        result = 1 if window == k else 0
        for i in range(k,n):
            window = len(set(s[i-k + 1:i+1]))
            result +=1 if window == k else 0
        return result
