from typing import List

def k_sum_subarrays(nums: List[int], k: int) -> int:
    # Write your code here
    count = 0
    prefix_sum = {0:1}
    curr_prefix_sum = 0

    for num in nums:
        curr_prefix_sum += num

        if curr_prefix_sum - k in prefix_sum:
            count += prefix_sum[curr_prefix_sum - k]
            
        freq = prefix_sum.get(curr_prefix_sum, 0)
        prefix_sum[curr_prefix_sum] = freq + 1

    return count

if __name__ == "__main__":
    nums = [1, 2, -1, 1, 2]
    k = 3

    print(k_sum_subarrays(nums, k))