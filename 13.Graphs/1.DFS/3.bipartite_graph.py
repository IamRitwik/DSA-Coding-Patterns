from typing import List

def bipartite_graph_validation(graph: List[List[int]]) -> bool:
    """
    Check if a graph is bipartite using DFS and 2-coloring.
    
    A graph is bipartite if we can color all nodes with 2 colors
    such that no two adjacent nodes have the same color.
    
    Time Complexity: O(V + E) where V = vertices, E = edges
    Space Complexity: O(V) for the colors array and recursion stack
    """
    # 0 = unvisited, 1 = color A, 2 = color B
    colors = [0] * len(graph)
    
    # Check each component (graph might be disconnected)
    for node in range(len(graph)):
        # If unvisited, try to color this component starting with color 1
        if colors[node] == 0:
            if not dfs(node, 1, graph, colors):
                return False
    
    return True


def dfs(node: int, color: int, graph: List[List[int]], colors: List[int]) -> bool:
    """
    Try to color the current node and all its neighbors.
    
    Returns True if coloring is successful (bipartite), False otherwise.
    """
    # Color the current node
    colors[node] = color
    
    # Determine the opposite color for neighbors
    next_color = 2 if color == 1 else 1
    
    # Check all neighbors
    for neighbor in graph[node]:
        # Case 1: Neighbor already has the SAME color -> conflict!
        if colors[neighbor] == color:
            return False
        
        # Case 2: Neighbor is unvisited -> try to color it with opposite color
        if colors[neighbor] == 0:
            if not dfs(neighbor, next_color, graph, colors):
                return False
    
    # All neighbors colored successfully
    return True


def main():
    # Test case from the problem
    graph = [[1, 4], [0, 2], [1], [4], [0, 3]]
    result = bipartite_graph_validation(graph)
    print(f"Graph: {graph}")
    print(f"Is Bipartite: {result}")
    print(f"Expected: True")
    
    # Test case: Non-bipartite graph (triangle)
    graph2 = [[1, 2], [0, 2], [0, 1]]
    result2 = bipartite_graph_validation(graph2)
    print(f"\nGraph: {graph2}")
    print(f"Is Bipartite: {result2}")
    print(f"Expected: False")


if __name__ == "__main__":
    main()