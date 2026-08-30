class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = [words[0]]
        prev = sorted(words[0])
        for word in words[1:]:
            curr = sorted(word)
            if curr != prev:
                res.append(word)
                prev = curr
        return res

