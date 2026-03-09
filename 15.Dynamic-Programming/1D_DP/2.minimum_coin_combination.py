from typing import Dict, List


def min_coin_combination(coins: List[int], target: int) -> int:
    """
    Returns the minimum number of coins needed to form `target` using denominations in `coins`.

    Recurrence (without memoization):
        Let T(x) be the minimum coins to make sum x.
        T(0) = 0
        T(x) = 1 + min_{coin in coins, coin <= x} T(x - coin), if any coin <= x, else inf

    Time complexity (without memoization):
        - Each state x can branch to up to k choices (k = len(coins)),
          leading to an exponential upper bound in target (roughly O(k^target)).
    Space complexity (without memoization):
        - O(target) recursion depth in the worst case.

    With memoization (this implementation via `top_down`):
        - Each sub-target x in [0, target] is computed at most once.
        - For each x we iterate over all k coins.

    Time complexity (with memoization):
        - O(target * k), where k = len(coins).
    Space complexity (with memoization):
        - O(target) for the memo dictionary plus O(target) recursion depth → O(target).
    """
    res = top_down(coins, target, {})
    return -1 if res == float('inf') else res

"""
Top-down approach with memoization
Time complexity: O(target * k)
Space complexity: O(target)
"""
def top_down(coins: List[int], target: int, memo: Dict[int, int]) -> int:
    # base case
    if target == 0:
        return 0

    if target in memo:
        return memo[target]

    min_coins = float("inf")

    for coin in coins:
        # avoid negative targets
        if coin <= target:
            min_coins = min(min_coins, 1 + top_down(coins, target - coin, memo))

    memo[target] = min_coins

    return memo[target]

def bottom_up(coins: List[int], target: int) -> int:
    dp = [float('inf')] * (target + 1)

    dp[0] = 0

    for t in range(1, target + 1):
        for coin in coins:
            if coin <= t:
                dp[t] = min(dp[t], 1 + dp[t - coin])
    
    return dp[target] if dp[target] != float('inf') else -1



def main() -> None:
    # Example 1: standard case
    coins = [1, 2, 5]
    target = 11
    # 11 can be formed as 5 + 5 + 1 → minimum 3 coins
    print(f"coins={coins}, target={target}, min_coins={min_coin_combination(coins, target)}")

    print(f"coins={coins}, target={target}, min_coins={bottom_up(coins, target)}")

    # Example 2: case where target cannot be formed exactly
    coins_impossible = [2, 4]
    target_impossible = 7
    # 7 cannot be formed using only 2 and 4 → expect -1
    print(
        f"coins={coins_impossible}, target={target_impossible}, "
        f"min_coins={min_coin_combination(coins_impossible, target_impossible)}"
    )

    print(
        f"coins={coins_impossible}, target={target_impossible}, "
        f"min_coins={bottom_up(coins_impossible, target_impossible)}"
    )


if __name__ == "__main__":
    main()
