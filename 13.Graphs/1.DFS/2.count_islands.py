from typing import List

def count_islands(matrix: List[List[int]]) -> int:
    """
    Count the number of islands in a 2D grid.
    
    Time Complexity: O(m * n) where m is the number of rows and n is the number of columns.
    - We visit each cell once in the nested loops.
    - DFS marks visited cells, so each cell is processed at most once.
    
    Space Complexity: O(m * n) in the worst case.
    - Recursive call stack can go as deep as m * n in the worst case (e.g., all cells are land forming one island).
    - The matrix is modified in-place, so no additional space for visited tracking.
    """
    if not matrix:
        return 0
    count = 0

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            # if a land cell is found, perform DFS to explore full island
            # add the count
            if matrix[r][c] == 1:
                dfs(r, c, matrix)
                count += 1
    return count

def dfs(r: int, c: int, matrix: List[List[int]]) -> None:
    # mark the current land cell visited
    matrix[r][c] = -1

    # direction vectors
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # recursively call DFS on each neighboring land cell to explore the island
    for d in dirs:
        next_r, next_c = r + d[0], c + d[1]
        if (is_within_bounds(next_r, next_c, matrix) and matrix[next_r][next_c] == 1):
            dfs(next_r, next_c, matrix)

def is_within_bounds(r: int, c: int, matrix: List[List[int]]) -> bool:
    return 0 <= r < len(matrix) and 0 <= c < len(matrix[0])

def main():
    # Test case: Grid with multiple islands
    # 1 represents land, 0 represents water
    matrix = [
        [1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]
    ]
    
    print("Input Grid:")
    for row in matrix:
        print(row)
    
    result = count_islands(matrix)
    print(f"\nNumber of islands: {result}")
    print("Expected: 6")
    
    # Test case 2: Single large island
    matrix2 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    
    print("\n" + "="*40)
    print("Test Case 2 - Single large island:")
    for row in matrix2:
        print(row)
    
    result2 = count_islands(matrix2)
    print(f"\nNumber of islands: {result2}")
    print("Expected: 1")
    
    # Test case 3: No islands
    matrix3 = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    
    print("\n" + "="*40)
    print("Test Case 3 - No islands:")
    for row in matrix3:
        print(row)
    
    result3 = count_islands(matrix3)
    print(f"\nNumber of islands: {result3}")
    print("Expected: 0")

if __name__ == "__main__":
    main()