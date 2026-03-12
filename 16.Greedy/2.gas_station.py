from typing import List

# Time Complexity: O(n)
# Space Complexity: O(1)
def gas_stations(gas: List[int], cost: List[int]) -> int:
    if sum(gas) < sum(cost):
        return -1
    
    start = tank = 0

    for i in range(len(gas)):
        tank += gas[i] - cost[i]

        if tank < 0:
            start, tank = i + 1, 0
            
    return start


def main() -> None:
    # Example test case
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    expected = 3  # Starting at station index 3 works
    result = gas_stations(gas, cost)
    print(f"gas_stations({gas}, {cost}) = {result} (expected {expected})")


if __name__ == "__main__":
    main()