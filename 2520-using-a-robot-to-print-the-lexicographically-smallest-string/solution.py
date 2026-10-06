class Solution:
    def robotWithString(self, s: str) -> str:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        # the top of t is <= the smallest letter still left in s.
        t = []
        p = []
        for ch in s:
            t.append(ch)
            count[ord(ch) - ord('a')] -= 1
            smallest_val = "{"
            for i in range(26):
                if count[i] > 0:
                    smallest_val = chr(ord('a') + i)
                    break
            while t and t[-1] <= smallest_val:
                p.append(t.pop())
        return "".join(p)
