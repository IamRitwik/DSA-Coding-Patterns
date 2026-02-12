class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = []


def graph_deep_copy(node: GraphNode) -> GraphNode:
    """
    Time Complexity: O(V + E) where V is the number of vertices (nodes) and E is the number of edges
    - We visit each node exactly once due to the clone_map
    - For each node, we iterate through all its neighbors (edges)
    
    Space Complexity: O(V) where V is the number of vertices
    - clone_map stores all V nodes
    - Recursion stack can go up to V depth in worst case (linear graph)
    """
    if not node:
        return None
    return dfs(node)

def dfs(node: GraphNode, clone_map = {}) -> GraphNode:
    # if already cloned, return from hashmap
    if node in clone_map:
        return clone_map[node]
    
    # clone the current node
    cloned_node = GraphNode(node.val)

    # add to hashmap
    clone_map[node] = cloned_node

    # iterate through the neighbours of current node to connect
    for neighbor in node.neighbors:
        cloned_neighbor = dfs(neighbor, clone_map)
        cloned_node.neighbors.append(cloned_neighbor)

    return cloned_node


def main():
    # Test case: Create a graph with cycles
    # Graph structure:
    #     1 --- 2
    #     |     |
    #     3 --- 4
    
    node1 = GraphNode(1)
    node2 = GraphNode(2)
    node3 = GraphNode(3)
    node4 = GraphNode(4)
    
    # Create bidirectional edges
    node1.neighbors = [node2, node3]
    node2.neighbors = [node1, node4]
    node3.neighbors = [node1, node4]
    node4.neighbors = [node2, node3]
    
    # Perform deep copy
    cloned_node1 = graph_deep_copy(node1)
    
    # Verify the copy is independent
    print("Original graph - Node 1 value:", node1.val)
    print("Cloned graph - Node 1 value:", cloned_node1.val)
    
    # Verify structure is preserved
    print("\nOriginal Node 1 neighbors:", [n.val for n in node1.neighbors])
    print("Cloned Node 1 neighbors:", [n.val for n in cloned_node1.neighbors])
    
    # Verify deep copy (different memory addresses)
    print("\nOriginal and cloned are different objects:", node1 is not cloned_node1)
    print("Original and cloned neighbors are different objects:", 
          node1.neighbors[0] is not cloned_node1.neighbors[0])
    
    # Modify original graph and verify clone is unaffected
    node1.val = 100
    print("\nAfter modifying original node value to 100:")
    print("Original Node 1 value:", node1.val)
    print("Cloned Node 1 value (should remain 1):", cloned_node1.val)


if __name__ == "__main__":
    main()
