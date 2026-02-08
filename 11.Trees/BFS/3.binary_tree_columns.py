from collections import defaultdict, deque
from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Time: O(N log N)
# Space: O(N)
def binary_tree_columns(root: TreeNode) -> List[List[int]]:
    # Write your code here
    if not root:
        return []
    col_map = defaultdict(list)
    leftmost_col = rightmost_col = 0
    # Queue stores: (node, row, col)
    queue = deque([(root, 0, 0)])

    while queue:
        node, row, col = queue.popleft()

        if node:
            # Store (row, val) to sort later
            col_map[col].append((row, node.val))
            leftmost_col = min(leftmost_col, col)
            rightmost_col = max(rightmost_col, col)

            queue.append((node.left, row + 1, col - 1))
            queue.append((node.right, row + 1, col + 1))

    result = []
    for i in range(leftmost_col, rightmost_col + 1):
        # Sort by row first (asc), then by value (asc)
        sorted_column = sorted(col_map[i], key=lambda x: (x[0], x[1]))
        # Extract just the values
        result.append([val for row, val in sorted_column])

    return result