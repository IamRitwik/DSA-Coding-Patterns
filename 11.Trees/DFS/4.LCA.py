class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Time: O(n) - visit each node once
# Space: O(h) - recursion stack depth (h = height of tree)
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Find the Lowest Common Ancestor (LCA) of two nodes in a binary tree.
    
    Key Insight:
    - If current node is p or q, it could be the LCA
    - If p and q are in different subtrees, current node is the LCA
    - If both are in same subtree, recurse into that subtree
    
    Returns:
    - The LCA node if both p and q exist in the tree
    - None if one or both nodes don't exist
    """
    # Base case: empty tree or found one of the target nodes
    if not root or root == p or root == q:
        return root
    
    # Search in left and right subtrees
    left_result = lowest_common_ancestor(root.left, p, q)
    right_result = lowest_common_ancestor(root.right, p, q)
    
    # Case 1: Found nodes in both subtrees → current node is LCA
    if left_result and right_result:
        return root
    
    # Case 2: Found in only one subtree → return that result
    # (either the LCA from that subtree, or one of p/q)
    return left_result if left_result else right_result


# Example usage and test
if __name__ == "__main__":
    # Build tree:
    #       3
    #      / \
    #     5   1
    #    / \ / \
    #   6  2 0  8
    #     / \
    #    7   4
    
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)
    
    # Test case 1: LCA of 5 and 1 should be 3
    p = root.left  # Node 5
    q = root.right  # Node 1
    result = lowest_common_ancestor(root, p, q)
    print(f"LCA of {p.val} and {q.val} is: {result.val}")  # Expected: 3
    
    # Test case 2: LCA of 5 and 4 should be 5
    p = root.left  # Node 5
    q = root.left.right.right  # Node 4
    result = lowest_common_ancestor(root, p, q)
    print(f"LCA of {p.val} and {q.val} is: {result.val}")  # Expected: 5
    
    # Test case 3: LCA of 6 and 7 should be 5
    p = root.left.left  # Node 6
    q = root.left.right.left  # Node 7
    result = lowest_common_ancestor(root, p, q)
    print(f"LCA of {p.val} and {q.val} is: {result.val}")  # Expected: 5
