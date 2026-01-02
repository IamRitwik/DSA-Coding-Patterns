from typing import List

def pair_sum_sorted(nums: List[int], target: int) -> List[int]:
    # Write your code here
    left, right = 0, len(nums) - 1

    while left < right:
        pair_sum = nums[left] + nums[right]
        if pair_sum < target:
            left += 1
        elif pair_sum > target:
            right -= 1
        else:
            return [left, right]
    return []

if __name__ == "__main__":
    nums = [-5, -2, 3, 4, 6]
    target = 7
    print(pair_sum_sorted(nums, target))