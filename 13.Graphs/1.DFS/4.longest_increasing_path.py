from typing import List

def longest_increasing_path(matrix: List[List[int]]) -> int:
    """
    Longest Increasing Path in a Matrix
    
    Time Complexity: O(m * n)
    Find the longest increasing path in a matrix.
    You can move up, down, left, or right from each cell.
    
    Time Complexity: O(m * n) where m = rows, n = columns
    - Each cell is visited once and its result is cached
    - DFS with memoization ensures each cell is computed only once
    
    Space Complexity: O(m * n)
    - memo array: O(m * n)
    - recursion stack: O(m * n) in worst case (entire matrix is increasing)
    """
    if not matrix:
        return 0
    
    res = 0
    m, n = len(matrix), len(matrix[0])
    memo = [[0] * n for _ in range(m)]

    for r in range(m):
        for c in range(n):
            res = max(res, dfs(r, c, matrix, memo))
    return res


def dfs(r: int, c: int, matrix: List[List[int]], memo: List[List[int]]) -> int:
    """
    DFS with memoization to find longest increasing path from cell (r, c).
    """
    # Return cached result if already computed
    if memo[r][c] != 0:
        return memo[r][c]
    
    max_path = 1  # Current cell counts as path length 1
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right

    for d in dirs:
        next_r, next_c = r + d[0], c + d[1]
        if (is_within_bounds(next_r, next_c, matrix) and 
            matrix[next_r][next_c] > matrix[r][c]):
            max_path = max(max_path, 1 + dfs(next_r, next_c, matrix, memo))

    memo[r][c] = max_path
    return max_path


def is_within_bounds(r: int, c: int, matrix: List[List[int]]) -> bool:
    """Check if position (r, c) is within matrix bounds."""
    return 0 <= r < len(matrix) and 0 <= c < len(matrix[0])


def main():
    # Test case 1: Standard matrix with clear increasing path
    matrix1 = [
        [9, 9, 4],
        [6, 6, 8],
        [2, 1, 1]
    ]
    result1 = longest_increasing_path(matrix1)
    print("Test Case 1:")
    print("Matrix:")
    for row in matrix1:
        print(row)
    print(f"Longest Increasing Path: {result1}")
    print(f"Expected: 4 (path: 1 → 2 → 6 → 9)")
    print()
    
    # Test case 2: Matrix with longer path
    matrix2 = [
        [3, 4, 5],
        [3, 2, 6],
        [2, 2, 1]
    ]
    result2 = longest_increasing_path(matrix2)
    print("Test Case 2:")
    print("Matrix:")
    for row in matrix2:
        print(row)
    print(f"Longest Increasing Path: {result2}")
    print(f"Expected: 4 (path: 3 → 4 → 5 → 6)")
    print()
    
    # Test case 3: Single element
    matrix3 = [[5]]
    result3 = longest_increasing_path(matrix3)
    print("Test Case 3:")
    print(f"Matrix: {matrix3}")
    print(f"Longest Increasing Path: {result3}")
    print(f"Expected: 1")
    print()
    
    # Test case 4: All same values
    matrix4 = [
        [1, 1, 1],
        [1, 1, 1]
    ]
    result4 = longest_increasing_path(matrix4)
    print("Test Case 4:")
    print("Matrix:")
    for row in matrix4:
        print(row)
    print(f"Longest Increasing Path: {result4}")
    print(f"Expected: 1 (no increasing path possible)")


if __name__ == "__main__":
    main()