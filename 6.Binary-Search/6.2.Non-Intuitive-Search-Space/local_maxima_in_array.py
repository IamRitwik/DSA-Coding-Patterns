from typing import List

# Time: O(logn)
# Space: O(1)
def local_maxima_in_array(nums: List[int]) -> int:
    # Write your code here
    left , right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left

if __name__ == "__main__":
    def is_peak(arr, index):
        if index < 0 or index >= len(arr):
            return False
        left_ok = (index == 0) or (arr[index] > arr[index - 1])
        right_ok = (index == len(arr) - 1) or (arr[index] > arr[index + 1])
        return left_ok and right_ok

    test_cases = [
        [1, 2, 3, 1],
        [1, 2, 1, 3, 5, 6, 4],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1],
        [1, 2],
        [2, 1],
        [1, 5, 1]
    ]

    print("Running tests...")
    for i, nums in enumerate(test_cases):
        idx = local_maxima_in_array(nums)
        valid = is_peak(nums, idx)
        print(f"Test {i+1}: Input {nums} -> Index {idx} (Value {nums[idx]}) -> {'Passed' if valid else 'Failed'}")