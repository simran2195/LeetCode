class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        # 2 ptrs for the doubly linked list
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} #map key to node

        # end nodes of doubly linked list
        #LRU -> left is LRU, right is most recently used
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        #update the MRU
        if key in self.cache:
            # remove from list and add to last (MRU)
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    # remove node from linked list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    #insert at right of linked list
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev = prev
        node.next = nxt

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key,value)
        # insert node to list
        self.insert(self.cache[key])

        # if after insertion len(cache) > capacity, then delete or evict the LRU from left
        if len(self.cache) > self.capacity:
            # find node for LRU using left ptr
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)