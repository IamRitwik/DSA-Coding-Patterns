from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Time: O(N)
# Space: O(H)
def kth_smallest_number_in_BST(root: TreeNode, k: int) -> int:
    result = []
    def dfs(node: TreeNode) -> None:
        if not node:
            return
        dfs(node.left)
        result.append(node.val)
        dfs(node.right)
    
    dfs(root)
    return result[k-1]
    

def main():
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)

    print(f"Kth Smallest Element is: {kth_smallest_number_in_BST(root, 3)}")


if __name__ == "__main__":
    main()

