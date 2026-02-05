"""
Binary Tree Maximum Path Sum - SIMPLIFIED EXPLANATION

Problem: Find the maximum sum of any path in a binary tree.

KEY INSIGHT:
At each node, we need to answer TWO questions:
1. What's the max path that PASSES THROUGH this node? (left + node + right)
2. What's the max path we can EXTEND to parent? (node + max(left, right))

We track #1 globally (the answer), and return #2 to help parent nodes.
"""

max_sum = float('-inf')

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Time: O(n)
# Space: O(h)
def max_path_sum(root: TreeNode) -> int:
    # Write your code here
    global max_sum
    dfs(root)
    return max_sum

def dfs(node: TreeNode) -> int:
    global max_sum

    # base case
    if not node:
        return 0
    
    # STEP 1: Get the best path sums from left and right subtrees
    # Use max(0, ...) to ignore negative paths (better to not include them)

    left_max = max(dfs(node.left), 0)
    right_max = max(dfs(node.right), 0)

    # STEP 2: Calculate the path sum that PASSES THROUGH this node
    # This is: left_path + current_node + right_path
    path_through_node = left_max + node.val + right_max

    # STEP 3: Update global maximum if this path is better
    max_sum = max(max_sum, path_through_node)

    # STEP 4: Return the max path we can EXTEND upward to parent
    # Parent can only use ONE branch (left OR right), not both
    return node.val + max(left_max, right_max)
