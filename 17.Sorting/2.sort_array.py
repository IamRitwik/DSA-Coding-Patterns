from typing import List


def sort_array(nums: List[int]) -> List[int]:
    # Time Complexity: Average O(n log n), Worst O(n^2)
    # Space Complexity: O(log n) for recursion stack, worst O(n)
    quicksort(nums, 0, len(nums) - 1)
    return nums


def quicksort(nums: List[int], left: int, right: int) -> None:
    # base case
    if left >= right:
        return
    
    # partition
    pivot_index = partition(nums, left, right)

    # recursive quicksort
    quicksort(nums, left, pivot_index - 1)
    quicksort(nums, pivot_index + 1, right)

def partition(nums: List[int], left: int, right: int) -> int:
    pivot = nums[right]

    lo = left

    for i in range(left, right):
        if nums[i] < pivot:
            nums[lo], nums[i] = nums[i], nums[lo]
            lo += 1

    nums[lo], nums[right] = nums[right], nums[lo]

    return lo


if __name__ == "__main__":
    # test case for sort_array
    nums = [5, 2, 3, 1, 4]
    print("Original array:", nums)
    sorted_nums = sort_array(nums)
    print("Sorted array:", sorted_nums)