from typing import Dict, Optional

# Time: O(1)
# Space: O(N)
class DoublyLinkedListNode:
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}

        # head and tail dummy nodes
        self.head = DoublyLinkedListNode(-1,-1)
        self.tail = DoublyLinkedListNode(-1,-1)

        # stitch head and tail together of the DLL
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_to_tail(self, node: DoublyLinkedListNode) -> None:
        prev_node = self.tail.prev
        node.prev = prev_node
        node.next = self.tail
        prev_node.next = node
        self.tail.prev = node

    def remove_node(self, node: DoublyLinkedListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1

        # remove the node of given key and add to tail of DLL
        self.remove_node(self.hashmap[key])
        self.add_to_tail(self.hashmap[key])
        return self.hashmap[key].val

    def put(self, key: int, value: int) -> None:
        # if key already in hashmap, remove the existing node
        if key in self.hashmap:
            self.remove_node(self.hashmap[key])
        
        # if key is new and we are at capacity, evict the LRU node
        elif len(self.hashmap) >= self.capacity:
            lru_node = self.head.next
            del self.hashmap[lru_node.key]
            self.remove_node(lru_node)

        # create and add the new node
        new_node = DoublyLinkedListNode(key, value)
        self.hashmap[key] = new_node
        self.add_to_tail(new_node)

if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(f"get(1): {cache.get(1)}") # returns 1
    cache.put(3, 3) # evicts key 2
    print(f"get(2): {cache.get(2)}") # returns -1 (not found)
    cache.put(4, 4) # evicts key 1
    print(f"get(1): {cache.get(1)}") # returns -1 (not found)
    print(f"get(3): {cache.get(3)}") # returns 3
    print(f"get(4): {cache.get(4)}") # returns 4

