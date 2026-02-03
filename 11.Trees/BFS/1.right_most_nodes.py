from collections import deque
from typing import List

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Time: O(n)
# Space: O(n)
def rightmost_nodes_of_a_binary_tree(root: TreeNode) -> List[int]:
    # Write your code here
    if not root:
        return []

    result = []
    q = deque([root])

    while q:
        level_size = len(q)

        for i in range(level_size):
            node = q.popleft()

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
            if i == level_size - 1:
                result.append(node.val)
    return result


if __name__ == "__main__":
    # Test Case: Create a binary tree
    #         1
    #        / \
    #       2   3
    #      / \   \
    #     4   5   6
    #    /         \
    #   7           8
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    root.left.left.left = TreeNode(7)
    root.right.right.right = TreeNode(8)
    
    result = rightmost_nodes_of_a_binary_tree(root)
    print(f"Rightmost nodes: {result}")
    print(f"Expected: [1, 3, 6, 8]")
    
    # Test Case 2: Single node
    single_node = TreeNode(10)
    result2 = rightmost_nodes_of_a_binary_tree(single_node)
    print(f"\nSingle node test: {result2}")
    print(f"Expected: [10]")
    
    # Test Case 3: Empty tree
    result3 = rightmost_nodes_of_a_binary_tree(None)
    print(f"\nEmpty tree test: {result3}")
    print(f"Expected: []")
