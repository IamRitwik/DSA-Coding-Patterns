from typing import List


# 0 - push LEFT
# 2 - push RIGHT
# 1 - stay in MIDDLE
# Time Complexity: O(n)
# Space Complexity: O(1)
def dutch_national_flag(nums: List[int]) -> None:
    i, left, right = 0, 0, len(nums) - 1

    while i <= right:
        if nums[i] == 0:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
            i += 1
        elif nums[i] == 2:
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1
        else:
            i += 1


if __name__ == "__main__":
    # test case for dutch_national_flag
    nums = [2, 0, 2, 1, 1, 0]
    print("Original array:", nums)
    dutch_national_flag(nums)
    print("Sorted (0s,1s,2s) array:", nums)