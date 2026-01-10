class MultiLevelListNode:
    def __init__(self, val, next=None, child=None) -> None:
        self.val = val
        self.next = next
        self.child = child

# Time: O(n)
# Space: O(1)
def flatten_multi_level_list(head: MultiLevelListNode) -> MultiLevelListNode:
    # Write your code here
    if not head:
        return None
    
    tail = head

    while tail.next:
        tail = tail.next
    
    curr = head

    while curr:
        if curr.child:
            tail.next = curr.child
            curr.child = None

            while tail.next:
                tail = tail.next
        curr = curr.next
        
    return head

def print_list(head: MultiLevelListNode):
    curr = head
    while curr:
        print(curr.val, end=" -> " if curr.next else "")
        curr = curr.next
    print()

if __name__ == "__main__":
    # Level 1: 1 -> 2 -> 3
    #          |
    # Level 2: 4 -> 5
    #               |
    # Level 3:      6
    
    n6 = MultiLevelListNode(6)
    n5 = MultiLevelListNode(5, child=n6)
    n4 = MultiLevelListNode(4, next=n5)
    n3 = MultiLevelListNode(3)
    n2 = MultiLevelListNode(2, next=n3)
    n1 = MultiLevelListNode(1, next=n2, child=n4)

    print("List before flattening:")
    print_list(n1) # Should only show Level 1: 1 -> 2 -> 3

    flattened_head = flatten_multi_level_list(n1)
    
    print("\nList after flattening:")
    print_list(flattened_head) # Expected: 1 -> 2 -> 3 -> 4 -> 5 -> 6