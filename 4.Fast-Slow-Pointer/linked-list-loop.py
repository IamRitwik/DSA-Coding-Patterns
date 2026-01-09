from typing import Optional, Any
from LinkedList import LinkedList, Node

# Time - O(N)
# Space - O(1)
def linked_list_loop(ll: LinkedList) -> bool:
    # slow and fast both start at the head
    slow = fast = ll.head

    # fast moves 2 steps, slow moves 1 step
    while fast and fast.next_node:
        fast = fast.next_node.next_node
        slow = slow.next_node

        # If they meet, there is a cycle
        if slow == fast:
            return True
    
    # If fast reaches the end, there is no cycle
    return False

if __name__ == "__main__":
    # Test Case 1: No Cycle
    print("Test Case 1: No Cycle")
    ll1 = LinkedList()
    ll1.insert_end(1)
    ll1.insert_end(2)
    ll1.insert_end(3)
    print(f"Has loop: {linked_list_loop(ll1)}")  # Expected: False

    # Test Case 2: With Cycle
    print("\nTest Case 2: With Cycle")
    ll2 = LinkedList()
    ll2.insert_end(10)
    ll2.insert_end(20)
    ll2.insert_end(30)
    ll2.insert_end(40)
    
    # Create a cycle: 40 -> 20
    # Head is 10. 10 -> 20 -> 30 -> 40 -> 20...
    node10 = ll2.head
    node20 = node10.next_node
    node30 = node20.next_node
    node40 = node30.next_node
    node40.next_node = node20
    
    print(f"Has loop: {linked_list_loop(ll2)}")  # Expected: True

    # Test Case 3: Empty List
    print("\nTest Case 3: Empty List")
    ll3 = LinkedList()
    print(f"Has loop: {linked_list_loop(ll3)}")  # Expected: False