from typing import List


class UnionFind:
    def __init__(self, size) -> None:
        # Time: O(n), Space: O(n) to initialize parent and size arrays
        self.parent = [i for i in range(size)]
        self.size = [1]*size
    
    def union(self, x: int, y: int) -> bool:
        # Amortized Time: ~O(α(n)) or O(1) due to path compression and union by size
        rep_x, rep_y = self.find(x), self.find(y)

        if rep_x != rep_y:
            if self.size[rep_x] > self.size[rep_y]:
                self.parent[rep_y] = rep_x
                self.size[rep_x] += self.size[rep_y]
            else:
                self.parent[rep_x] = rep_y
                self.size[rep_y] += self.size[rep_x]
            # return True if both groups are merged
            return True
        # return False if both points belong to same group
        return False
    
    def find(self, x: int) -> int:
        # Amortized Time: ~O(α(n)) with path compression, Space: O(1) extra
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    

def connect_the_dots(points: List[List[int]]) -> int:
    # Let n be the number of points.
    # We build all possible edges: O(n^2) edges and O(n^2) space.
    # Sorting edges: O(n^2 log n^2) = O(n^2 log n).
    # Kruskal’s loop processes all edges: O(n^2 * α(n)) amortized with Union-Find (O(1) amortized time).
    # Overall Time: O(n^2 log n), Space: O(n^2).
    n = len(points)
    edges = []

    for i in range(n):
        for j in range(i + 1, n):
            # calculate manhattan distance
            cost = (abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]))
            edges.append((cost, i, j))
    
    # sort edges in ascending order
    edges.sort()
    uf = UnionFind(n)
    total_cost = edges_added = 0

    # Kruskal's algorithm
    for cost, p1, p2 in edges:
        # if points are not connected , connect them
        # add to total_cost
        if uf.union(p1, p2):
            total_cost += cost
            edges_added += 1
            # if n - 1 edges have been added to MST, MST is complete
            if edges_added == n - 1:
                return total_cost
    return 0


if __name__ == "__main__":
    # Example test case (LeetCode 1584)
    points = [[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]
    expected = 20  # known minimum total cost
    result = connect_the_dots(points)
    print(f"Points: {points}")
    print(f"Minimum cost to connect all points: {result}")
    print(f"Expected: {expected}")