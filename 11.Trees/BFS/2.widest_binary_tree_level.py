from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Time: O(n)
# Space: O(n)
def widest_binary_tree_level(root: TreeNode) -> int:
    # Write your code here
    if not root:
        return 0
    
    max_width = 0
    q = deque([(root, 0)]) # stores (node, index) pair

    while q:
        level_size = len(q)

        left_most_index = q[0][1]
        right_most_index = left_most_index

        for _ in range(level_size):
            node, i = q.popleft()

            if node.left:
                q.append((node.left, 2*i + 1))
            if node.right:
                q.append((node.right, 2*i + 2))
            right_most_index = i
        max_width = max(max_width, right_most_index - left_most_index + 1)
    
    return max_width


if __name__ == "__main__":
    # Test Case 1: Tree with gaps (null nodes)
    #         1
    #        / \
    #       2   3
    #      /     \
    #     4       5
    #    /         \
    #   6           7
    # Width at each level: [1, 2, 2, 2]
    # Max width = 2 (but considering gaps/null nodes, it's actually 8 at bottom level)
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(6)
    root.right.right.right = TreeNode(7)
    
    result = widest_binary_tree_level(root)
    print(f"Test 1 - Tree with gaps:")
    print(f"Max width: {result}")
    print(f"Expected: 8 (distance from leftmost to rightmost node at bottom level)\n")
    
    # Test Case 2: Complete binary tree
    #         1
    #        / \
    #       2   3
    #      / \
    #     4   5
    # Width at each level: [1, 2, 2]
    # Max width = 2
    
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)
    
    result2 = widest_binary_tree_level(root2)
    print(f"Test 2 - Complete binary tree:")
    print(f"Max width: {result2}")
    print(f"Expected: 2\n")
    
    # Test Case 3: Single node
    single_node = TreeNode(10)
    result3 = widest_binary_tree_level(single_node)
    print(f"Test 3 - Single node:")
    print(f"Max width: {result3}")
    print(f"Expected: 1\n")
    
    # Test Case 4: Empty tree
    result4 = widest_binary_tree_level(None)
    print(f"Test 4 - Empty tree:")
    print(f"Max width: {result4}")
    print(f"Expected: 0\n")
    
    # Test Case 5: Skewed tree (only left children)
    #     1
    #    /
    #   2
    #  /
    # 3
    root5 = TreeNode(1)
    root5.left = TreeNode(2)
    root5.left.left = TreeNode(3)
    
    result5 = widest_binary_tree_level(root5)
    print(f"Test 5 - Left-skewed tree:")
    print(f"Max width: {result5}")
    print(f"Expected: 1")