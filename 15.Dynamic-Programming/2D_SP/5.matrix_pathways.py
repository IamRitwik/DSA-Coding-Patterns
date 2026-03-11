# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
def matrix_pathways(m: int, n: int) -> int:
    dp = [[1] * n for _ in range(m)]
    #base case is dp[0][0] = 1

    for r in range(1, m):
        for c in range(1, n):
            #path to current cell = path from above + path from left
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
            
    return dp[m - 1][n - 1]


def main() -> None:
    # Example test case
    m, n = 3, 3
    expected = 6
    result = matrix_pathways(m, n)
    print(f"matrix_pathways({m}, {n}) = {result} (expected {expected})")


if __name__ == "__main__":
    main()