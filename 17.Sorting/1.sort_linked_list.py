class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def merge_sort(head: ListNode) -> ListNode:
    # Time Complexity: O(n log n)
    # Space Complexity: O(log n) for recursion stack
    # if linked list is empty or having only 1 element
    if not head or not head.next:
        return head
    
    # split the linked list
    second_half = split_list(head)

    # recursively sort both halves
    first_half_sorted = merge_sort(head)
    second_half_sorted = merge_sort(second_half)

    # merge sorted lists
    return merge(first_half_sorted, second_half_sorted)

def split_list(head: ListNode) -> ListNode:
    slow = fast = head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    
    second_head = slow.next
    slow.next = None
    return second_head

def merge(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)

    tail = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    
    tail.next = l1 or l2
    return dummy.next


def print_list(head: ListNode) -> None:
    curr = head
    values = []
    while curr:
        values.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(values))


if __name__ == "__main__":
    # create a test linked list: 4 -> 2 -> 1 -> 3
    node1 = ListNode(4)
    node2 = ListNode(2)
    node3 = ListNode(1)
    node4 = ListNode(3)

    node1.next = node2
    node2.next = node3
    node3.next = node4

    print("Original list:")
    print_list(node1)

    sorted_head = merge_sort(node1)

    print("Sorted list:")
    print_list(sorted_head)