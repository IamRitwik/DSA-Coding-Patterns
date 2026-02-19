from typing import List


# Time complexity:
# - For each element, we have two choices: include it or exclude it.
# - This gives 2^n different subsets for an input of size n.
# - For each subset, copying the current subset into the result costs up to O(n) in the worst case.
# Overall time complexity: O(n * 2^n).
#
# Space complexity:
# - The recursion depth is at most n, and the current subset holds at most n elements.
# - Ignoring the returned result, the auxiliary space is O(n).
# Overall space complexity: O(n × 2^n) including the output, and O(n) auxiliary.
def find_all_subsets(nums: List[int]) -> List[List[int]]:
    res: List[List[int]] = []
    backtrack(0, [], nums, res)
    return res


def backtrack(i: int, curr_subset: List[int], nums: List[int], res: List[List[int]]) -> None:
    # base case
    if i == len(nums):
        res.append(curr_subset[:])
        return

    # include current element and recursively explore all paths
    curr_subset.append(nums[i])

    # explore branches recursively(INCLUDING nums[i])
    backtrack(i + 1, curr_subset, nums, res)

    # exclude current element and recursively explore all paths
    curr_subset.pop()

    # explore branches recursively(EXCLUDING nums[i])
    backtrack(i + 1, curr_subset, nums, res)


if __name__ == "__main__":
    nums = [1, 2, 3]
    subsets = find_all_subsets(nums)
    print(f"Input: {nums}")
    print("All subsets:")
    for s in subsets:
        print(s)