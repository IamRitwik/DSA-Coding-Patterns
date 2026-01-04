from typing import List

def pair_sum_unsorted(nums: List[int], target: int) -> List[int]:
    # Write your code here
    num_map = {}

    # for i,x in enumerate(nums):
    #     num_map[x] = i

    # for i, x in enumerate(nums):
    #     complement = target - x
    #     if complement in num_map and num_map[complement] != i:
    #         return [i, num_map[complement]]

    for i, x in enumerate(nums):
        complement = target - x
        if complement in num_map:
            return [num_map[complement], i]
        num_map[x] = i

    return []


if __name__ == "__main__":
    nums = [-1, 3, 4, 2]
    target = 3

    print(pair_sum_unsorted(nums, target))