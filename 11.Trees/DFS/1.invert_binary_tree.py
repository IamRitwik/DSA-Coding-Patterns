class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

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