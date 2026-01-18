from typing import List

def matrix_search(matrix: List[List[int]], target: int) -> bool:
    # Write your code here
    m, n = len(matrix), len(matrix[0])

    left, right = 0, m*n - 1

    while left <= right:
        mid = (left + right) // 2
        # i = r*n +c
        r, c = mid // n, mid % n
        
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False

if __name__ == "__main__":
    matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
    target = 10

    print(matrix_search(matrix, target))