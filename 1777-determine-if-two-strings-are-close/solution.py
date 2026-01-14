class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        # check if both contain same set of keys
        if set(counter1.keys()) != set(counter2.keys()):
            return False
        #now check the set of values of its the same meaning letters can be swapped 
        
        return sorted(counter1.values()) == sorted(counter2.values())







