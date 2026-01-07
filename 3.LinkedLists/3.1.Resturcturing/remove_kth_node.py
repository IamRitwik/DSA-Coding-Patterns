from LinkedList import LinkedList, Node

def remove_kth_last_node(head: LinkedList, k: int) -> None:
    # Write your code here
    dummy = Node(-1)
    dummy.next_node = ll.head
    leader, trailer = dummy, dummy

    for _ in range(k):
        leader = leader.next_node
        if not leader:
            return
    
    while leader.next_node:
        leader = leader.next_node
        trailer = trailer.next_node
    
    trailer.next_node = trailer.next_node.next_node


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_start(4) 
    ll.insert_start(2)  
    ll.insert_start(1)  
    ll.insert_end(7)    
    ll.insert_end(3)    
    ll.traverse()

    remove_kth_last_node(ll, 2)

    ll.traverse()