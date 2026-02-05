# Binary Tree Maximum Path Sum - Simplified Explanation

**Problem**: Find the maximum sum of any path in a binary tree.

## Key Insight
At each node, we need to answer **TWO** questions:

1. **What's the max path that PASSES THROUGH this node?**
   - Formula: `left_max + node.val + right_max`
   - This path CANNOT be extended to the parent (because that would branch three ways).
   - We track this value globally to find the ultimate answer.

2. **What's the max path we can EXTEND to parent?**
   - Formula: `node.val + max(left_max, right_max)`
   - This is what we return to the parent node so it can calculate its own paths.

## The Solution

Here is the implementation using a valid Python approach to handle the global maximum variable.

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def max_path_sum(root: TreeNode) -> int:
    # Use a list to avoid global variable scope issues
    # (One could also use 'nonlocal' keyword in Python 3)
    max_sum = [float('-inf')]
    
    def dfs(node):
        """
        Returns: Maximum path sum that can be extended upward from this node
        Side effect: Updates max_sum[0] with best path found so far
        """
        # Base case: empty node contributes 0
        if not node:
            return 0
        
        # STEP 1: Get the best path sums from left and right subtrees
        # Use max(0, ...) to ignore negative paths (better to not include them)
        left_max = max(0, dfs(node.left))
        right_max = max(0, dfs(node.right))
        
        # STEP 2: Calculate the path sum that PASSES THROUGH this node
        # This is: left_path + current_node + right_path
        path_through_node = left_max + node.val + right_max
        
        # STEP 3: Update global maximum if this path is better
        max_sum[0] = max(max_sum[0], path_through_node)
        
        # STEP 4: Return the max path we can EXTEND upward to parent
        # Parent can only use ONE branch (left OR right), not both
        return node.val + max(left_max, right_max)
    
    dfs(root)
    return max_sum[0]
```

## Step-by-Step Trace

Let's trace a simple example to see how the recursion works.

**Tree Structure:**
```
     1
    / \
   2   3
```

**Execution Order (Post-Order Traversal):**

1. **Visit Node 2 (Leaf)**
   - `left_max` = 0 (no child)
   - `right_max` = 0 (no child)
   - `path_through_node` (2 itself) = 0 + 2 + 0 = **2**
   - Global `max_sum` becomes **2**
   - **Returns** to parent: 2 + max(0,0) = **2**

2. **Visit Node 3 (Leaf)**
   - `left_max` = 0
   - `right_max` = 0
   - `path_through_node` (3 itself) = 0 + 3 + 0 = **3**
   - Global `max_sum` becomes max(2, 3) = **3**
   - **Returns** to parent: 3 + max(0,0) = **3**

3. **Visit Node 1 (Root)**
   - `left_max` (from node 2) = max(0, 2) = **2**
   - `right_max` (from node 3) = max(0, 3) = **3**
   - `path_through_node` = 2 + 1 + 3 = **6**
   - Global `max_sum` becomes max(3, 6) = **6** (The Answer!)
   - **Returns** to parent: 1 + max(2, 3) = 4 (unused since this is root)

**Final Answer:** 6

## Examples

### Example 1: Tree with Negative Values
```
    -10
    /  \
   9   20
      /  \
     15   7
```
- **Process**: The algorithm will ignore the `-10` when calculating the path for the subtree rooted at `20` if connecting them reduces the sum.
- However, the optimal path is `15 -> 20 -> 7`.
- **Sum**: 15 + 20 + 7 = **42**

### Example 2: Single Node
```
     5
```
- **Sum**: **5**
