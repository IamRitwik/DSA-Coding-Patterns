memo = {}


def climbing_stairs(n: int) -> int:
    """
    Recurrence relation:
        f(n) = f(n - 1) + f(n - 2)
        f(1) = 1, f(2) = 2

    Time Complexity: O(n), because each state from 1..n is computed once
    and then reused via memoization.
    Space Complexity: O(n), for the memo dictionary that stores up to n
    subproblem results and the recursion stack depth.
    """
    # base case
    if n <= 2:
        return n

    if n in memo:
        return memo[n]

    memo[n] = climbing_stairs(n - 1) + climbing_stairs(n - 2)

    return memo[n]


def climbing_stairs_bottom_up(n: int) -> int:
    """
    Iterative DP using the same recurrence:
        f(n) = f(n - 1) + f(n - 2)

    Time Complexity: O(n), we fill the DP array once from 1..n.
    Space Complexity: O(n), due to the DP array of size n + 1.
    """
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)

    # base case
    dp[1], dp[2] = 1, 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


if __name__ == "__main__":
    # Test cases for climbing_stairs
    n_values = [1, 2, 3, 4, 5]
    for n in n_values:
        print(f"Number of ways to climb {n} stairs -> top-down:", climbing_stairs(n))
        print(f"Number of ways to climb {n} stairs -> bottom-up:", climbing_stairs_bottom_up(n))