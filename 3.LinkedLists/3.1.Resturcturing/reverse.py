from LinkedList import LinkedList

# Time - O(n)
# Space - O(1)
def reverse(ll: LinkedList) -> None:
    prev = None
    current = ll.head
    while current:
        next_node = current.next_node
        current.next_node = prev
        prev = current
        current = next_node
    ll.head = prev

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_start(3)  # [3]
    ll.insert_start(2)  # [2, 3]
    ll.insert_start(1)  # [1, 2, 3]
    ll.insert_end(4)    # [1, 2, 3, 4]
    ll.insert_end(5)    # [1, 2, 3, 4, 5]
    ll.insert_start(0)  # [0, 1, 2, 3, 4, 5]
    ll.traverse()

    reverse(ll)
    ll.traverse()