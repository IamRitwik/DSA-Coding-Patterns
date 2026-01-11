from typing import List

# Time - O(nlogn) + O(n^2) = O(n^2)
# Space -  O(n) auxilary space for sorting, O(n^2) worst case considering output
def triplet_sum(nums: List[int]) -> List[List[int]]:
    # Write your code here
    triplets = []
    nums.sort()
    for i in range(len(nums)):
        # optimization: triplets consisting of positive numbers can never sum to 0 as 
        # list is sorted
        if nums[i] > 0:
            break
        # avoid duplicate, skip 'a' if its same
        if i > 0 and nums[i] == nums[i-1]:
            continue
        #find all pairs that sum up tp -a (-nums[i])
        pairs = pair_sum_sorted_all_pairs(nums, i+1, -nums[i])
        
        for pair in pairs:
            triplets.append([nums[i]] + pair)
    return triplets
    
def pair_sum_sorted_all_pairs(nums: List[int], start: int, target: int) -> List[List[int]]:
    pairs = []
    left, right = start, len(nums) - 1

    while left < right:
        pair_sum = nums[left] + nums[right]
        if pair_sum == target:
            pairs.append([nums[left], nums[right]])
            left += 1

            # avoid duplicate, skip 'b' if its same
            while left < right and nums[left] == nums[left - 1]:
                left += 1
        elif pair_sum < target:
            left += 1
        else:
            right -= 1
    return pairs



if __name__ == "__main__":
    nums = [0, -1, 2, -3, 1]
    print(triplet_sum(nums))
    #triplet_sum(nums)