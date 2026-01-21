class Solution:
    def equalFrequency(self, word: str) -> bool:
        for i in range(len(word)):
            temp = word[:i] + word[i+1:]
            freq = Counter(temp)
            freq_dist = freq.values()
            if len(set(freq_dist)) == 1:
                return True
        return False
