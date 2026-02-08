from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def preorder_serialize(node, serialized_list) -> None:
    # base case
    if node is None:
        serialized_list.append('#')
        return
    serialized_list.append(str(node.val))
    preorder_serialize(node.left, serialized_list)
    preorder_serialize(node.right, serialized_list)

# Time: O(N)
# Space: O(N)
def serialize(root: TreeNode) -> str:
    # Pre-Order Traversal
    serialized_list = []
    preorder_serialize(root, serialized_list)
    return ",".join(serialized_list)

def deserialize(data: str) -> TreeNode:
    node_values = iter(data.split(','))
    return build_tree(node_values)

def build_tree(values: List[str]) -> TreeNode:
     val = next(values)

     # base case
     if val == '#':
        return None
     
     node = TreeNode(int(val))
     node.left = build_tree(values)
     node.right = build_tree(values)
     return node

