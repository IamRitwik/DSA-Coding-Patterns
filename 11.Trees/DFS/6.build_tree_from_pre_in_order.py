from typing import List

# Tracks current position in preorder array
preorder_index = 0
inorder_index_map = {}

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Time: O(n) - visit each node once
# Space: O(h) - recursion stack depth (h = height of tree)
def build_binary_tree(preorder: List[int], inorder: List[int]) -> TreeNode:
    global inorder_index_map

    # populate the inorder_index_map
    for i, val in enumerate(inorder):
        inorder_index_map[val] = i
    
    return build_subtree(0, len(inorder) - 1, preorder, inorder)

def build_subtree(left: int, right: int, preorder: List[int], inorder: List[int]) -> TreeNode:
    global preorder_index, inorder_index_map

    # base case
    if left > right:
        return None

    val = preorder[preorder_index]

    inorder_index = inorder_index_map[val]

    node = TreeNode(val)

    preorder_index += 1

    node.left = build_subtree(
        left, inorder_index - 1, preorder, inorder
    )

    node.right = build_subtree(
        inorder_index + 1, right, preorder, inorder
    )

    return node


# Helper function to verify the tree structure
def level_order_traversal(root: TreeNode) -> List:
    """Returns level-order traversal with None for missing nodes"""
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    
    return result


# Test cases
if __name__ == "__main__":
    # Test case 1: Example from problem
    print("Test Case 1:")
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    
    # Reset global variables
    preorder_index = 0
    inorder_index_map = {}
    
    root = build_binary_tree(preorder, inorder)
    result = level_order_traversal(root)
    expected = [3, 9, 20, None, None, 15, 7]
    
    print(f"Preorder:  {preorder}")
    print(f"Inorder:   {inorder}")
    print(f"Result:    {result}")
    print(f"Expected:  {expected}")
    print(f"✓ PASS" if result == expected else "✗ FAIL")
    print()
    
    # Test case 2: Single node
    print("Test Case 2: Single node")
    preorder = [1]
    inorder = [1]
    
    preorder_index = 0
    inorder_index_map = {}
    
    root = build_binary_tree(preorder, inorder)
    result = level_order_traversal(root)
    expected = [1]
    
    print(f"Preorder:  {preorder}")
    print(f"Inorder:   {inorder}")
    print(f"Result:    {result}")
    print(f"Expected:  {expected}")
    print(f"✓ PASS" if result == expected else "✗ FAIL")
    print()
    
    # Test case 3: Left-skewed tree
    print("Test Case 3: Left-skewed tree")
    preorder = [1, 2, 3]
    inorder = [3, 2, 1]
    
    preorder_index = 0
    inorder_index_map = {}
    
    root = build_binary_tree(preorder, inorder)
    result = level_order_traversal(root)
    expected = [1, 2, None, 3]
    
    print(f"Preorder:  {preorder}")
    print(f"Inorder:   {inorder}")
    print(f"Result:    {result}")
    print(f"Expected:  {expected}")
    print(f"✓ PASS" if result == expected else "✗ FAIL")
    print()
    
    # Test case 4: Right-skewed tree
    print("Test Case 4: Right-skewed tree")
    preorder = [1, 2, 3]
    inorder = [1, 2, 3]
    
    preorder_index = 0
    inorder_index_map = {}
    
    root = build_binary_tree(preorder, inorder)
    result = level_order_traversal(root)
    expected = [1, None, 2, None, 3]
    
    print(f"Preorder:  {preorder}")
    print(f"Inorder:   {inorder}")
    print(f"Result:    {result}")
    print(f"Expected:  {expected}")
    print(f"✓ PASS" if result == expected else "✗ FAIL")
    print()
    
    # Test case 5: Complete binary tree
    print("Test Case 5: Complete binary tree")
    preorder = [1, 2, 4, 5, 3, 6, 7]
    inorder = [4, 2, 5, 1, 6, 3, 7]
    
    preorder_index = 0
    inorder_index_map = {}
    
    root = build_binary_tree(preorder, inorder)
    result = level_order_traversal(root)
    expected = [1, 2, 3, 4, 5, 6, 7]
    
    print(f"Preorder:  {preorder}")
    print(f"Inorder:   {inorder}")
    print(f"Result:    {result}")
    print(f"Expected:  {expected}")
    print(f"✓ PASS" if result == expected else "✗ FAIL")

