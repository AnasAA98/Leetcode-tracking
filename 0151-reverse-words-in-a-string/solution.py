class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        word = []
        for ch in s:
            if ch == " ":
                if word:
                    stack.append("".join(word))
                    word = []
            else:
                word.append(ch)
        if word:
            stack.append("".join(word))

        res = []
        for i in range(len(stack) -1, -1, -1):
            res.append(stack[i])
        return " ".join(res)
