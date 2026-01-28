class RandomizedSet:

    def __init__(self):
        self.map = {}  # val,index
        self.nums = []  # index -> val

    def insert(self, val: int) -> bool:
        result = True if val not in self.map else False
        if result:
            self.nums.append(val)
            index = len(self.nums) - 1
            self.map[val] = index
        return result         
    def remove(self, val: int) -> bool:
        # to remove it will be a simple  swap operation between val[index] and val[-1]
        res = True if val in self.map else False
        if res:
            index = self.map[val]
            last_val = self.nums[-1]
            self.nums[index] = last_val
            self.nums.pop()
            self.map[last_val] = index
            del self.map[val]
        return res

    def getRandom(self) -> int:
        return random.choice(self.nums)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
