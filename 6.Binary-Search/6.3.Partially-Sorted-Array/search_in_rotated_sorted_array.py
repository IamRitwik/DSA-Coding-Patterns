from typing import List

# Time: O(logn)
# Space: O(1)
def find_the_target_in_a_rotated_sorted_array(nums: List[int], target: int) -> int:
    # Write your code here
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # check if left sub array is sorted
        # and target is in the rane
        elif nums[left] <= nums[mid]:

            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        else:    
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return - 1            
                 


if __name__ == "__main__":
    nums = [8, 9, 1, 2, 3, 4, 5, 6, 7]
    target = 1

    print(find_the_target_in_a_rotated_sorted_array(nums, target))