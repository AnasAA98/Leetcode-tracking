class Node:
    
    def __init__(self,key,val):
        self.key, self.val = key, val
        self.next= self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key: node
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self, node: Node):
        a = node.prev
        b = node.next
        a.next = b
        b.prev = a

    def insert(self, node: Node):
        mru = self.right.prev
        mru.next = node
        node.next = self.right
        self.right.prev = node
        node.prev = mru

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key,value)
        self.cache[key] = node
        self.insert(node)
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
