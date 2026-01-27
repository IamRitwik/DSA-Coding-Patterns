import heapq
from typing import List


# Definition of ListNode:
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
    
    def __lt__(self, other):
        return self.val < other.val

# Time - O(klogk) + O(nlogk), space - O(k)
def combine_sorted_linked_lists(lists: List[ListNode]) -> ListNode:
    min_heap = []

    # add heads of all lists to min heap
    for head in lists:
        if head:
            heapq.heappush(min_heap, head)
    
    # dummy node
    dummy = ListNode(-1)

    # pointer to dummy node
    curr = dummy

    while min_heap:
        # pop the node with smallest value and add to new list
        smallest_node = heapq.heappop(min_heap)
        curr.next = smallest_node
        curr = curr.next

        # push sub-sequent nodes to heap
        if smallest_node.next:
            heapq.heappush(min_heap, smallest_node.next)

    return dummy.next


def create_linked_list(arr: List[int]) -> ListNode:
    """Helper function to create a linked list from an array"""
    if not arr:
        return None
    
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


def print_linked_list(head: ListNode) -> None:
    """Helper function to print a linked list"""
    values = []
    curr = head
    while curr:
        values.append(str(curr.val))
        curr = curr.next
    print(" → ".join(values) if values else "Empty list")


if __name__ == "__main__":
    # Test case: Merge 3 sorted linked lists
    print("Test Case: Merge K Sorted Lists")
    print("=" * 50)
    
    # Create 3 sorted linked lists
    list1 = create_linked_list([1, 4, 5])
    list2 = create_linked_list([1, 3, 4])
    list3 = create_linked_list([2, 6])
    
    print("\nInput Lists:")
    print("List 1: ", end="")
    print_linked_list(list1)
    print("List 2: ", end="")
    print_linked_list(list2)
    print("List 3: ", end="")
    print_linked_list(list3)
    
    # Merge the lists
    merged = combine_sorted_linked_lists([list1, list2, list3])
    
    print("\nMerged List: ", end="")
    print_linked_list(merged)
    print("\nExpected:    1 → 1 → 2 → 3 → 4 → 4 → 5 → 6")
    
    # Edge case: Empty lists
    print("\n" + "=" * 50)
    print("Edge Case: Empty and single element lists")
    list4 = create_linked_list([])
    list5 = create_linked_list([1])
    merged2 = combine_sorted_linked_lists([list4, list5])
    print("Merged: ", end="")
    print_linked_list(merged2)
    print("Expected: 1")