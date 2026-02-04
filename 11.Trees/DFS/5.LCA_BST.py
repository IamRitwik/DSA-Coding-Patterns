class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def lowest_common_ancestor_bst_recursive(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Find LCA in a Binary Search Tree (BST) - Recursive approach
    
    BST Property: left < root < right
    
    Key Insight:
    - If both p and q are SMALLER than root → LCA is in LEFT subtree
    - If both p and q are LARGER than root → LCA is in RIGHT subtree
    - Otherwise → current root is the LCA (split point)
    
    Time: O(h) where h is height (O(log n) balanced, O(n) skewed)
    Space: O(h) for recursion stack
    """
    # Both nodes are in left subtree
    if p.val < root.val and q.val < root.val:
        return lowest_common_ancestor_bst_recursive(root.left, p, q)
    
    # Both nodes are in right subtree
    elif p.val > root.val and q.val > root.val:
        return lowest_common_ancestor_bst_recursive(root.right, p, q)
    
    # Split point: one is on left, one is on right (or one equals root)
    else:
        return root


def lowest_common_ancestor_bst_iterative(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Find LCA in a BST - Iterative approach (MOST OPTIMAL)
    
    Time: O(h) where h is height
    Space: O(1) - no recursion!
    """
    current = root
    
    while current:
        # Both nodes are in left subtree
        if p.val < current.val and q.val < current.val:
            current = current.left
        
        # Both nodes are in right subtree
        elif p.val > current.val and q.val > current.val:
            current = current.right
        
        # Found the split point - this is the LCA
        else:
            return current
    
    return None  # Should never reach here if p and q exist in tree


# For comparison: General Binary Tree approach (works but not optimal for BST)
def lowest_common_ancestor_binary_tree(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    General binary tree LCA - works for BST but NOT optimal
    
    Time: O(n) - may visit all nodes
    Space: O(h) - recursion stack
    """
    if not root or root == p or root == q:
        return root
    
    left_result = lowest_common_ancestor_binary_tree(root.left, p, q)
    right_result = lowest_common_ancestor_binary_tree(root.right, p, q)
    
    if left_result and right_result:
        return root
    
    return left_result if left_result else right_result


if __name__ == "__main__":
    # Build BST:
    #       6
    #      / \
    #     2   8
    #    / \ / \
    #   0  4 7  9
    #     / \
    #    3   5
    
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    
    print("BST Structure:")
    print("      6")
    print("     / \\")
    print("    2   8")
    print("   / \\ / \\")
    print("  0  4 7  9")
    print("    / \\")
    print("   3   5")
    print()
    
    # Test cases
    test_cases = [
        (root.left, root.right, 6),  # LCA(2, 8) = 6
        (root.left, root.left.right, 2),  # LCA(2, 4) = 2
        (root.left.right.left, root.left.right.right, 4),  # LCA(3, 5) = 4
        (root.left.left, root.left.right.right, 2),  # LCA(0, 5) = 2
    ]
    
    print("=" * 70)
    print("COMPARING THREE APPROACHES")
    print("=" * 70)
    
    for i, (p, q, expected) in enumerate(test_cases, 1):
        print(f"\nTest {i}: LCA({p.val}, {q.val})")
        print(f"Expected: {expected}")
        
        result1 = lowest_common_ancestor_bst_recursive(root, p, q)
        result2 = lowest_common_ancestor_bst_iterative(root, p, q)
        result3 = lowest_common_ancestor_binary_tree(root, p, q)
        
        print(f"  BST Recursive:  {result1.val} {'✅' if result1.val == expected else '❌'}")
        print(f"  BST Iterative:  {result2.val} {'✅' if result2.val == expected else '❌'}")
        print(f"  Binary Tree:    {result3.val} {'✅' if result3.val == expected else '❌'}")
    
    print("\n" + "=" * 70)
    print("PERFORMANCE COMPARISON")
    print("=" * 70)
    print("\n1. BST RECURSIVE:")
    print("   ✅ Time: O(h) - only visits nodes on one path")
    print("   ⚠️  Space: O(h) - recursion stack")
    print("   ✅ Clean and easy to understand")
    
    print("\n2. BST ITERATIVE:")
    print("   ✅ Time: O(h) - only visits nodes on one path")
    print("   ✅ Space: O(1) - no recursion!")
    print("   ✅ MOST OPTIMAL for BST")
    
    print("\n3. BINARY TREE (Your current code):")
    print("   ⚠️  Time: O(n) - may visit ALL nodes")
    print("   ⚠️  Space: O(h) - recursion stack")
    print("   ✅ Works for ANY binary tree (not just BST)")
    
    print("\n" + "=" * 70)
    print("VISUAL EXAMPLE: LCA(0, 5)")
    print("=" * 70)
    print("\nBST Approach (visits 3 nodes):")
    print("  6 → both 0,5 < 6, go LEFT")
    print("  2 → both 0,5 in this subtree, but 0 < 2 < 5, SPLIT! Return 2 ✅")
    print("\nBinary Tree Approach (visits 7 nodes):")
    print("  Must search BOTH left and right subtrees at each node")
    print("  Visits: 6, 2, 0, 4, 3, 5, 8 (then backtracks)")
    print("=" * 70)
