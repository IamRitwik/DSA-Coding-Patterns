class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Recursive approach
# Time: O(n)
# Space: O(h)
def invert_binary_tree(root: TreeNode) -> TreeNode:
    # Base case: node is null, nothing to invert
    if not root:
        return None
    
    # swap the left and right sub trees of root
    root.left, root.right = root.right, root.left

    # recursively invert the left and right sub trees
    invert_binary_tree(root.left)
    invert_binary_tree(root.right)

    return root


# Iterative approach
# Time: O(n)
# Space: O(h)
def invert_binary_tree_iterative(root: TreeNode) -> TreeNode:
    if not root:
        return None
    
    stack = [root]

    while stack:
        node = stack.pop()

        node.left, node.right = node.right, node.left

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return root