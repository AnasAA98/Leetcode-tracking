class Node:
    def __init__(self,key,val):
        # node(key,val), node.val = (key,val)
        self.key, self.val = key, val
        self.next = self.prev = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key: node, val: pointer to Node in LinkedList
        self.left, self.right = Node(0,0), Node(0,0) # dummy nodes at left and right
        self.left.next = self.right
        self.right.prev = self.left

    def remove(self,node: Node):
        a = node.prev
        b = node.next
        a.next = b
        b.prev = a
    
    def insert(self, node: Node):
        lru = self.right.prev
        lru.next = node
        node.prev = lru
        node.next = self.right
        self.right.prev = node    
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
