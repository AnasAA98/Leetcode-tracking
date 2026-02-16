class Solution:
    def reverseWords(self, s: str) -> str:
        list_s = s.split()
        result = []
        for i in range(len(list_s)-1,-1,-1):
            result.append(list_s[i])
        return " ".join(result)

