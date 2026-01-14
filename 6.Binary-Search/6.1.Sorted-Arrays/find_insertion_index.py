from typing import List

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



if __name__ == "__main__":
    nums = [1, 2, 4, 5, 7, 8, 9]
    target = 4

    print(find_the_insertion_index(nums, target))

    nums = [1, 2, 4, 5, 7, 8, 9]
    target = 6

    print(find_the_insertion_index(nums, target))