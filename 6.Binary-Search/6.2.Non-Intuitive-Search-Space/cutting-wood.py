from typing import List

# Binary search upper bound pattern
# find last valid
# last position where condition succeeds
# Time: O(log(max(heights)) * n)
# Space: O(1)
def cutting_wood(heights: List[int], k: int) -> int:
    # Write your code here
    left, right = 0, max(heights)

    while left < right:

        # bias mid point towards right for upper bound binary search
        mid = (left + right) // 2 + 1

        if cuts_enough_wood(mid, k, heights):
            left = mid
        else:
            right = mid - 1
    return right


def cuts_enough_wood(H: int, k: int, heights: List[int]) -> bool:
    wood_collected = 0

    for height in heights:
        if height > H:
            wood_collected += (height - H)
    return wood_collected >= k

if __name__ == "__main__":
    heights = [2, 6, 3, 8]
    k = 7

    print(cutting_wood(heights, k))
