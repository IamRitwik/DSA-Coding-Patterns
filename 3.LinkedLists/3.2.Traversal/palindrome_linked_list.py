from typing import Optional, Any
from LinkedList import LinkedList, Node

# Time - O(N)
# Space - O(1)
def palindromic_linked_list(ll: LinkedList) -> bool:
    # Write your code here
    # find the middle of the linked list
    mid = find_middle(ll)
    print(f"mid point = {mid.data} - {mid}")
    # reverse the 2nd half of linked list starting at mid point
    second_half = reverse_list(mid)
    print(f"2nd half head point = {second_half.data} - {second_half}")

    ptr1 = ll.head
    ptr2 = second_half

    while ptr2:
        if ptr1.data != ptr2.data:
            return False
        ptr1, ptr2 = ptr1.next_node, ptr2.next_node
    return True


def find_middle(ll: LinkedList) -> Node:
    slow = fast = ll.head
    while fast and fast.next_node:
        slow = slow.next_node
        fast = fast.next_node.next_node
    return slow

def reverse_list(head: Node) -> Node:
    prev, current = None, head
    while current:
        next_node = current.next_node
        current.next_node = prev
        prev = current
        current = next_node
    return prev

if __name__ == "__main__":
    ll = LinkedList() 
    ll.insert_end(1)    
    ll.insert_end(2)    
    ll.insert_end(3)   
    ll.insert_end(2) 
    ll.insert_end(1) 
    ll.traverse()

    print(palindromic_linked_list(ll))

    