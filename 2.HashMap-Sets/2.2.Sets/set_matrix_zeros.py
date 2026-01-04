from typing import List

# Time - O(M * N) where M is rows and N is columns
# Space - O(M + N) to store unique row and column indices
def zero_striping(matrix: List[List[int]]) -> None:
    if not matrix or not matrix[0]:
        return
    m, n = len(matrix), len(matrix[0])
    zero_rows, zero_cols = set(), set()

    for r in range(m):
        for c in range(n):
            if matrix[r][c] == 0:
                zero_rows.add(r)
                zero_cols.add(c)
    # print(zero_rows)
    # print(zero_cols)

    for r in range(m):
        for c in range(n):
            if r in zero_rows or c in zero_cols:
                matrix[r][c] = 0


if __name__ == "__main__":
    matrix = [
        [1,2,3],
        [4,0,5],
        [6,7,8]
    ]
    
    zero_striping(matrix)

    matrix_2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    zero_striping(matrix_2)

    print(matrix)
    print(matrix_2)