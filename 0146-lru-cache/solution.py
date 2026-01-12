class Node:
    def __init__(self,key=0,val=0,next=None,prev=None):
        self.key = key
        self.val = val
        self.next,self.prev = next,prev
class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.capacity = capacity
        self.head,self.tail = Node(0,0), Node(0,0)
        self.head.next,self.tail.prev=self.tail,self.head
    
    def inset_front(self, node):
        last = self.tail.prev
        last.next = node
        node.prev = last
        node.next = self.tail
        self.tail.prev = node
    
    def remove(self, node):
        prev,nex = node.prev, node.next
        prev.next,nex.prev = nex, prev

    def get(self, key: int) -> int:
        if key in self.map:
            result = self.map[key]
            self.remove(result)
            self.inset_front(result)
            return result.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.remove(node)
            self.inset_front(node)
            return
        if len(self.map) == self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.map[lru.key]
        node = Node(key,value)
        self.map[key] = node
        self.inset_front(node)
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
