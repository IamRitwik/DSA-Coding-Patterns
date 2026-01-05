from typing import List

# Time - O(N)
# Space - O(N)
def longest_chain_of_consecutive_numbers(nums: List[int]) -> int:
    # Write your code here
    if not nums:
        return 0
    
    num_set = set(nums)
    print(num_set)
    longest_chain = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_chain = 1

            while (current_num+1) in num_set:
                current_num += 1
                current_chain += 1
            longest_chain = max(longest_chain, current_chain)
    return longest_chain


if __name__ == "__main__":
    nums = [1, 6, 2, 5, 8, 7, 10, 3]
    print(longest_chain_of_consecutive_numbers(nums))