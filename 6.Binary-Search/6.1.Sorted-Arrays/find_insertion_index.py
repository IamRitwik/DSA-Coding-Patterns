from typing import List

"""
Time - O(logN)
Space - O(1)
"""

def find_the_insertion_index(nums: List[int], target: int) -> int:
    # Write your code here
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2

        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left


"""
This is a key difference between two binary search patterns:

Pattern 1: left <= right (Classic Binary Search)
Used for finding exact matches
Search space: [left, right] (both inclusive)
Updates: right = mid - 1 or left = mid + 1
Terminates when left > right

Pattern 2: left < right (Lower/Upper Bound)
Used for finding insertion positions or boundaries
Search space: [left, right) (left inclusive, right exclusive)
Updates: right = mid or left = mid + 1
Terminates when left == right
Returns left (or right, they're equal)

"""


if __name__ == "__main__":
    nums = [1, 2, 4, 5, 7, 8, 9]
    target = 4

    print(find_the_insertion_index(nums, target))

    nums = [1, 2, 4, 5, 7, 8, 9]
    target = 6

    print(find_the_insertion_index(nums, target))