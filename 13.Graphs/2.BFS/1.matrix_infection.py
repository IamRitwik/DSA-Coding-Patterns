from collections import deque
from typing import List

def matrix_infection(matrix: List[List[int]]) -> int:
    """
    Matrix Infection / Rotting Oranges Problem
    
    Time Complexity: O(m * n)
    - Initial scan: O(m * n) to count fresh oranges and find all rotten oranges
    - BFS traversal: Each cell is visited at most once, so O(m * n)
    - Overall: O(m * n) where m = rows, n = columns
    
    Space Complexity: O(m * n)
    - Queue can hold at most all cells in worst case: O(m * n)
    - Directions array: O(1)
    - Overall: O(m * n)
    """
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque()
    ones = seconds = 0

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 1:
                ones += 1
            elif matrix[r][c] == 2:
                queue.append((r, c))
    
    # use level-order traversal
    while queue and ones > 0:
        seconds += 1
        for _ in range(len(queue)):
            r, c = queue.popleft()
            # infect the neighboring 1s and add them to queue
            for d in dirs:
                next_r, next_c = r + d[0], c + d[1]
                if (is_within_bounds(next_r, next_c, matrix) and matrix[next_r][next_c] == 1):
                    matrix[next_r][next_c] = 2
                    ones -= 1
                    queue.append((next_r, next_c))

    return seconds if ones == 0 else -1

def is_within_bounds(r: int, c: int, matrix: List[List[int]]) -> bool:
    return 0 <= r < len(matrix) and 0 <= c < len(matrix[0])


def main():
    # Test Case 1: Standard case - all oranges can rot
    print("Test Case 1: Standard case")
    matrix1 = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]
    result1 = matrix_infection(matrix1)
    print(f"Input: {[[2, 1, 1], [1, 1, 0], [0, 1, 1]]}")
    print(f"Output: {result1}")
    print(f"Expected: 4")
    print(f"Test {'PASSED' if result1 == 4 else 'FAILED'}\n")
    
    # Test Case 2: Impossible case - isolated fresh orange
    print("Test Case 2: Impossible case - isolated fresh orange")
    matrix2 = [
        [2, 1, 1],
        [0, 0, 0],
        [1, 0, 0]
    ]
    result2 = matrix_infection(matrix2)
    print(f"Input: {[[2, 1, 1], [0, 0, 0], [1, 0, 0]]}")
    print(f"Output: {result2}")
    print(f"Expected: -1")
    print(f"Test {'PASSED' if result2 == -1 else 'FAILED'}\n")
    
    # Test Case 3: All already rotten
    print("Test Case 3: All already rotten")
    matrix3 = [
        [2, 2, 2],
        [2, 2, 2]
    ]
    result3 = matrix_infection(matrix3)
    print(f"Input: {[[2, 2, 2], [2, 2, 2]]}")
    print(f"Output: {result3}")
    print(f"Expected: 0")
    print(f"Test {'PASSED' if result3 == 0 else 'FAILED'}\n")
    
    # Test Case 4: No fresh oranges
    print("Test Case 4: No fresh oranges")
    matrix4 = [
        [0, 2, 0],
        [0, 0, 0]
    ]
    result4 = matrix_infection(matrix4)
    print(f"Input: {[[0, 2, 0], [0, 0, 0]]}")
    print(f"Output: {result4}")
    print(f"Expected: 0")
    print(f"Test {'PASSED' if result4 == 0 else 'FAILED'}\n")
    
    # Test Case 5: Multiple rotten sources
    print("Test Case 5: Multiple rotten sources")
    matrix5 = [
        [2, 1, 1],
        [1, 1, 1],
        [1, 1, 2]
    ]
    result5 = matrix_infection(matrix5)
    print(f"Input: {[[2, 1, 1], [1, 1, 1], [1, 1, 2]]}")
    print(f"Output: {result5}")
    print(f"Expected: 2")
    print(f"Test {'PASSED' if result5 == 2 else 'FAILED'}\n")


if __name__ == "__main__":
    main()
