from collections import defaultdict
import heapq
from typing import List

def shortest_path(n: int, edges: List[List[int]], start: int) -> List[int] | List[float]:
    # Dijkstra (min-heap) on an adjacency list (non-negative weights).
    #
    # Let V = n (nodes), E = len(edges) (undirected edges).
    # - Build adjacency list: O(V + E) time, O(V + E) space.
    # - Each heap push/pop costs O(log V). In the usual implementation, we may push
    #   multiple entries for the same node (we skip stale ones via the distances check),
    #   but the total number of pushes is O(E), so:
    #   Time: O((V + E) log V)
    # - Distances array is O(V); heap can hold up to O(E) entries in worst case.
    #   Space: O(V + E)

    # step 1: build the adjacency list
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    # step 2: distance array
    distances = [float('inf')]*n
    distances[start] = 0

    # step 3: min-heap
    min_heap = [(0, start)] # distance, node

    # step 4: process nodes in increasing order
    while min_heap:
        curr_dist, node = heapq.heappop(min_heap)

        # skip if we already found a better path
        if curr_dist > distances[node]:
            continue

        # step 5: relax the edges
        for neighbor, weight in graph[node]:
            new_dist = curr_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(min_heap, (new_dist, neighbor))

    return [-1 if dist == float('inf') else dist for dist in distances]


if __name__ == "__main__":
    # Example graph:
    # 0 --1-- 1 --2-- 2
    #  \      |
    #   4     3
    #    \    |
    #       3
    n = 4
    edges = [
        [0, 1, 1],
        [1, 2, 2],
        [0, 3, 4],
        [1, 3, 3],
    ]
    start = 0
    result = shortest_path(n, edges, start)
    print(f"Shortest distances from node {start}: {result}")
    # Expected: [0, 1, 3, 4]