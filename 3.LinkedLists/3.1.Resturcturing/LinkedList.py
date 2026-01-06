class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.num_of_nodes = 0

    # O(1) constant running time
    def size(self):
        return self.num_of_nodes
    
    # O(1) constant running time
    def insert_start(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        # List is empty
        if not self.head:
            self.head = new_node
        # List is not empty
        else:
            new_node.next_node = self.head # type: ignore
            self.head = new_node

    # O(n) linear running time
    def insert_end(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)
        # List is empty
        if not self.head:
            self.head = new_node
        # List is not empty
        else:
            temp = self.head
            # this is why O(n) linear running time complexity
            while temp.next_node is not None:
                temp = temp.next_node
            temp.next_node = new_node # type: ignore

    # O(n) linear running time
    def traverse(self) -> None:
        current = self.head
        elements = []
        while current is not None:
            elements.append(current.data)
            current = current.next_node
        print(" -> ".join(str(element) for element in elements))

    # O(n) linear running time
    def remove(self, data):
        if not self.head:
            return None
        current = self.head
        prev_node = None
        # we have to track the previous node for future pointer updates
        while current is not None and current.data != data:
            prev_node = current
            current = current.next_node
        # search miss
        if not current:
            return None
        # update the references so we have the data we want to remove
        self.num_of_nodes -= 1  # Fix: decrement size
        if prev_node is None:
            self.head = current.next_node
        else:
            prev_node.next_node = current.next_node
        return current.data

    # O(1) constant running time
    def remove_start(self):
        """Remove and return the first element"""
        if not self.head:
            return None
        
        removed_data = self.head.data
        self.head = self.head.next_node
        self.num_of_nodes -= 1
        return removed_data

    # O(n) linear running time
    def remove_end(self):
        """Remove and return the last element"""
        if not self.head:
            return None
        
        # Only one node
        if self.head.next_node is None:
            removed_data = self.head.data
            self.head = None
            self.num_of_nodes -= 1
            return removed_data
        
        # Multiple nodes - find second to last
        current = self.head
        while current.next_node.next_node is not None:  # type: ignore
            current = current.next_node # type: ignore
        
        removed_data = current.next_node.data  # type: ignore
        current.next_node = None # type: ignore
        self.num_of_nodes -= 1
        return removed_data

    # O(n) linear running time
    def get(self, index: int):
        """Get element at specific index (0-based)"""
        if index < 0 or index >= self.num_of_nodes:
            raise IndexError(f"Index {index} out of range")
        
        current = self.head
        for _ in range(index):
            current = current.next_node  # type: ignore
        
        return current.data  # type: ignore

    # O(n) linear running time
    def insert_at(self, index: int, data):
        """Insert element at specific index (0-based)"""
        if index < 0 or index > self.num_of_nodes:
            raise IndexError(f"Index {index} out of range")
        
        # Insert at beginning
        if index == 0:
            self.insert_start(data)
            return
        
        # Insert at end
        if index == self.num_of_nodes:
            self.insert_end(data)
            return
        
        # Insert in middle
        new_node = Node(data)
        current = self.head
        for _ in range(index - 1):
            current = current.next_node  # type: ignore
        
        new_node.next_node = current.next_node  # type: ignore
        current.next_node = new_node  # type: ignore
        self.num_of_nodes += 1





if __name__ == "__main__":
    print("\n" + "🔗" * 25)
    print("LINKED LIST TESTING SUITE")
    print("🔗" * 25)

    ll = LinkedList()
    ll.insert_start(3)  # [3]
    ll.insert_start(2)  # [2, 3]
    ll.insert_start(1)  # [1, 2, 3]
    ll.insert_end(4)    # [1, 2, 3, 4]
    ll.insert_end(5)    # [1, 2, 3, 4, 5]
    ll.insert_start(0)  # [0, 1, 2, 3, 4, 5]
    ll.traverse()