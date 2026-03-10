from typing import List

def neighborhood_burglary(houses: List[int]) -> int:
    if not houses:
        return 0
    
    if len(houses) == 1:
        return houses[0]

    dp = [0] * len(houses)

    # base case:
    dp[0] = houses[0]
    dp[1] = max(houses[0], houses[1])

    for i in range(2, len(houses)):
        dp[i] = max(dp[i - 1], houses[i] + dp[i - 2])
    
    print(dp)

    return dp[len(houses) - 1]


if __name__ == "__main__":
    # Example test case
    houses = [2, 7, 9, 3, 1]
    result = neighborhood_burglary(houses)
    print(f"Maximum amount that can be robbed from {houses}: {result}")