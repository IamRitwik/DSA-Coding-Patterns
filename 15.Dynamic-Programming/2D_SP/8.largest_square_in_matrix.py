from typing import List

def largest_square_in_a_matrix(matrix: List[List[int]]) -> int:
    # Write your code here
    if not matrix:
        return 0

    m, n = len(matrix), len(matrix[0])

    dp = [[0] * n for _ in range(m)]

    max_len = 0

    # base case:
    for j in range(n):
        if matrix[0][j] == 1:
            dp[0][j] = 1
            max_len = 1
    
    for i in range(m):
        if matrix[i][0] == 1:
            dp[i][0] = 1
            max_len = 1
    
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 1:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1])
            max_len = max(max_len, dp[i][j])
    
    return max_len ** 2


def main() -> None:
    # Example test case (classic maximal square)
    matrix = [
        [1, 0, 1, 0, 0],
        [1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 0, 0, 1, 0],
    ]
    expected = 4  # largest all-1s square is 2x2, so area = 4
    result = largest_square_in_a_matrix(matrix)
    print(f"largest_square_in_a_matrix(matrix) = {result} (expected {expected})")


if __name__ == "__main__":
    main()