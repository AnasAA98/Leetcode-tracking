class MagicDictionary:

    def __init__(self):
        self.my_dict = defaultdict(int)
        self.my_set = set()
    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.my_set.add(word)
            for i in range(len(word)):
                candidate = word[:i] + '*' + word[i+1:]
                self.my_dict[candidate] += 1

    def search(self, searchWord: str) -> bool:
        in_set = searchWord in self.my_set
        for i in range(len(searchWord)):
            key = searchWord[:i] + '*' + searchWord[i+1:]
            if key not in self.my_dict:
                continue
            if self.my_dict[key] >= 2:
                return True
            if not in_set:
                return True
            
        return False

            

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
