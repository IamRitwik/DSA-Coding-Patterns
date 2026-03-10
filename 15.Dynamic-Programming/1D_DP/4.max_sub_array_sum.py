from typing import List

# Time: O(n) Space: O(1)
def maximum_subarray_sum(nums: List[int]) -> float:
    if not nums:
        return 0

    curr_sum = max_sum = nums[0]

    for i in range(1, len(nums)):
        curr_sum = max(curr_sum + nums[i], nums[i])
        max_sum = max(curr_sum, max_sum)
    
    return max_sum


if __name__ == "__main__":
    # Example test case
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = maximum_subarray_sum(nums)
    print(f"Maximum subarray sum for {nums}: {result}")