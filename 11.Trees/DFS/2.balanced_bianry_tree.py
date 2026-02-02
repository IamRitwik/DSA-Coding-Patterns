class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def balanced_binary_tree_validation(root: TreeNode) -> bool:
    # Write your code here
    return get_height(root) != -1

def get_height(node: TreeNode) -> int:
    if not node:
        return 0
    
    left_height = get_height(node.left)
    right_height = get_height(node.right)

    if left_height == -1 or right_height == -1:
        return -1
    if abs(left_height - right_height) > 1:
        return -1
    return 1 + max(left_height, right_height)
