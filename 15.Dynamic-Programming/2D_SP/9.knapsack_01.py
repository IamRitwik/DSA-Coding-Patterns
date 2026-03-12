from typing import List

# Time Complexity: O(n * k)
# Space Complexity: O(n * k)
def knapsack(k: int, weights: List[int], values: List[int]) -> int:
    n = len(values)

    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(n - 1, -1, -1):
        for c in range(1, k + 1):
            if weights[i] <= c:
                dp[i][c] = max(values[i] + dp[i + 1][c - weights[i]], dp[i + 1][c])
            else:
                dp[i][c] = dp[i + 1][c]

    return dp[0][k]


def main() -> None:
    # Example test case for 0/1 knapsack
    k = 50
    weights = [10, 20, 30]
    values = [60, 100, 120]
    expected = 220  # Take items with weight 20 and 30
    result = knapsack(k, weights, values)
    print(f"knapsack({k}, {weights}, {values}) = {result} (expected {expected})")


if __name__ == "__main__":
    main()