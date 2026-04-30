class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        sentence = s.split(" ")
        return " ".join(sentence[:k])
