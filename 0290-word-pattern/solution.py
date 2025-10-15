class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        mapping ={}
        for p,w in zip(pattern,words):
            if p in mapping and mapping[p] != w:
                return False
            elif p not in mapping and w in mapping.values():
                return False
            mapping[p] = w
        expected = [mapping[ch] for ch in pattern]
        return expected == words


