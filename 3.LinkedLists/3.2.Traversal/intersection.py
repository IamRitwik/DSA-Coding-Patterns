from typing import Optional
from LinkedList import LinkedList, Node

def linked_list_intersection(list_A: LinkedList, list_B: LinkedList) -> Optional[Node]:
    # Write your code here 
    ptr_A: Optional[Node] = list_A.head
    ptr_B: Optional[Node] = list_B.head

    while ptr_A != ptr_B:
        ptr_A = ptr_A.next_node if ptr_A else list_B.head

        ptr_B = ptr_B.next_node if ptr_B else list_A.head
    
    return ptr_A

if __name__ == "__main__":
    # Create nodes for the common part
    common = Node(7)
    common.next_node = Node(3)

    # List A: 1 -> 2 -> 4 -> 7 -> 3
    list_a = LinkedList()
    list_a.head = Node(1)
    list_a.head.next_node = Node(2)
    list_a.head.next_node.next_node = Node(4)
    list_a.head.next_node.next_node.next_node = common

    # List B: 9 -> 7 -> 3
    list_b = LinkedList()
    list_b.head = Node(9)
    list_b.head.next_node = common

    print("List A:")
    list_a.traverse()
    print("List B:")
    list_b.traverse()

    result = linked_list_intersection(list_a, list_b)
    
    if result:
        print(f"Intersection found at node with data: {result.data}")
    else:
        print("No intersection found")