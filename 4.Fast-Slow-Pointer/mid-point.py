from typing import Optional, Any
from LinkedList import LinkedList, Node

# Time - O(N)
# Space - O(1)
def linked_list_midpoint(ll: LinkedList) -> int:
    # slow and fast both start at the head
    slow = fast = ll.head

    # fast moves 2 steps, slow moves 1 step
    while fast and fast.next_node:
        fast = fast.next_node.next_node
        slow = slow.next_node

    return slow.data

def mid_point_1st(ll: LinkedList) -> int:
    slow = fast = ll.head

    while fast and fast.next_node:
        fast = fast.next_node.next_node
        slow = slow.next_node

        if fast.next_node.next_node == None:
            break
    return slow.data


if __name__ == "__main__":
    # Test Case 1: No Cycle
    print("Test Case 1: No Cycle")
    ll = LinkedList()
    ll.insert_end(1)
    ll.insert_end(2)
    ll.insert_end(3)
    ll.insert_end(10)
    ll.insert_end(20)
    ll.insert_end(30)

    ll.traverse()

    print(f"Mid Point (2nd middle) =  {linked_list_midpoint(ll)}") 

    print(f"Mid Point (1st middle) =  {mid_point_1st(ll)}") 

    