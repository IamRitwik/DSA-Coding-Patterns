class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Time: O(N)
# Space: O(H)
def binary_tree_symmetry(root: TreeNode) -> bool:
    # Write your code here
    if not root:
        return True
    return dfs(root.left, root.right)

def dfs(node1: TreeNode, node2: TreeNode) -> bool:
    # base case: both nodes null
    if not node1 and not node2:
        return True
    
    # one is null other isn't
    if not node1 or not node2:
        return False
    
    # check value of current nodes
    if node1.val != node2.val:
        return False
    
    # check node1's left subtree to node2's right subtree
    if not dfs(node1.left, node2.right):
        return False
    
    # check node1's right subtree with node2's left subtree
    return dfs(node1.right, node2.left)


if __name__ == '__main__':
    # Test Case 1: Symmetric Tree
    #      1
    #    /   \
    #   2     2
    #  / \   / \
    # 3   4 4   3
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(4)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(3)

    print(f"Test Case 1 (Symmetric): {binary_tree_symmetry(root1)}")

    # Test Case 2: Asymmetric Tree
    #      1
    #    /   \
    #   2     2
    #    \     \
    #     3     3
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.left.right = TreeNode(3)
    root2.right.right = TreeNode(3)

    print(f"Test Case 2 (Asymmetric): {binary_tree_symmetry(root2)}")