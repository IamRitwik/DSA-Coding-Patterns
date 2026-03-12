from typing import List

# Time Complexity: O(n)
# Space Complexity: O(n)
def candies(ratings: List[int]) -> int:
    n = len(ratings)

    candies = [1]*n

    # first pass: left neighbors
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # second pass: right neighbors
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    
    return sum(candies)


def main() -> None:
    # Example test case
    ratings = [1, 0, 2]
    expected = 5
    result = candies(ratings)
    print(f"candies({ratings}) = {result} (expected {expected})")


if __name__ == "__main__":
    main()