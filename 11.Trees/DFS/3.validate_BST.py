from typing import Optional


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Time: O(n) - visit each node once
# Space: O(h) - recursion stack depth (h = height of tree)
def binary_search_tree_validation(root: TreeNode) -> bool:
    """
    Validate if a binary tree is a valid BST.
    
    Key Pattern to Remember:
    - Each node must be within a valid range [min, max]
    - Left child: update MAX to parent's value
    - Right child: update MIN to parent's value
    """
    def validate(node: Optional[TreeNode], min_val: float, max_val: float) -> bool:
        # Empty tree is valid BST
        if not node:
            return True
        
        # Current node must be in valid range
        if not (min_val < node.val < max_val):
            return False
        
        # Check both subtrees with updated bounds
        return (validate(node.left, min_val, node.val) and    # left: max becomes node.val
                validate(node.right, node.val, max_val))       # right: min becomes node.val
    
    return validate(root, float('-inf'), float('inf'))


# Test case
if __name__ == "__main__":
    # Valid BST:     5
    #               / \
    #              3   7
    #             / \
    #            2   4
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(7)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    
    print(f"Valid BST: {binary_search_tree_validation(root)}")  # True
    
    # Invalid BST:   5
    #               / \
    #              3   7
    #             / \
    #            2   6  <- 6 is in left subtree but > 5
    root2 = TreeNode(5)
    root2.left = TreeNode(3)
    root2.right = TreeNode(7)
    root2.left.left = TreeNode(2)
    root2.left.right = TreeNode(6)
    
    print(f"Invalid BST: {binary_search_tree_validation(root2)}")  # False
