class RandomizedSet:

    def __init__(self):
        self.mapNum = {}
        self.listNum = []

    def insert(self, val: int) -> bool:
        res = val not in self.mapNum
        if res:
            self.mapNum[val] = len(self.listNum)
            self.listNum.append(val)
            
        return res

    def remove(self, val: int) -> bool:
        res = val in self.mapNum
        if res:
            index = self.mapNum[val]
            lastVal = self.listNum[-1]
            self.listNum[index] = lastVal
            self.listNum.pop()
            self.mapNum[lastVal] = index
            del self.mapNum[val]
        return res

    def getRandom(self) -> int:
        return random.choice(self.listNum)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

