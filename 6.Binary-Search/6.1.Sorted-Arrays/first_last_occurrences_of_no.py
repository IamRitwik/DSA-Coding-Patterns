from typing import List

def first_and_last_occurrences_of_a_number(nums: List[int], target: int) -> List[int]:
    # Write your code here
    if not nums:
        return [-1,-1]
    
    first_occur = lower_bound(nums, target)

    if first_occur >= len(nums) or nums[first_occur] != target:
        return [-1,-1]
    
    last_occur = upper_bound(nums, target) - 1

    return [first_occur, last_occur]

    
def lower_bound(nums: List[int], target: int):
    left, right = 0 , len(nums)

    while left < right:
        mid = (left + right) // 2  # Calculate mid INSIDE the loop
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left

# find 1st invalid index where element is greater than target
# first position where condition fails
def upper_bound(nums: List[int], target: int):
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2  # Calculate mid INSIDE the loop
        if nums[mid] > target:
            right = mid
        else:
            left = mid + 1
    return left
        

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11]
    target = 4

    print(first_and_last_occurrences_of_a_number(nums, target))

    nums = [1, 2, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    target = 3

    print(first_and_last_occurrences_of_a_number(nums, target))