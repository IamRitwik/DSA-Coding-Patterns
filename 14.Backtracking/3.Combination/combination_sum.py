from typing import List


# Time complexity:
# - Elements can be reused (we pass i, not i+1), allowing multiple combinations.
# - In the worst case, the recursion tree explores all possible ways to sum to target.
# - The depth is bounded by target/min(nums), and at each level we branch for each available number.
# - Worst case time complexity: O(N^(target/min(nums))) where N is the number of elements.
# - More practically, it's exponential: O(2^target/min(nums)) in the worst case.
#
# Space complexity:
# - The recursion depth is at most target/min(nums) (if we keep adding the smallest element).
# - The current combination list holds at most target/min(nums) elements.
# - Ignoring the output, auxiliary space is O(target/min(nums)).
# - The output list stores all valid combinations, which can be exponential in number.
# Overall space complexity: Exponential including output, O(target/min(nums)) auxiliary.
def combinations_of_sum_k(nums: List[int], target: int) -> List[List[int]]:
    res = []
    dfs([], 0, nums, target, res)
    return res

def dfs(combination: List[int], start_index: int, nums: List[int], target: int, res: List[List[int]]) -> None:
    # base case : if target == 0 we found combination
    if target == 0:
        res.append(combination[:])
        return

    if target < 0:
        return
    
    for i in range(start_index, len(nums)):

        # add the current number to create a combination
        combination.append(nums[i])

        # recursively explore all paths
        dfs(combination, i, nums, target - nums[i], res)

        # backtrack
        combination.pop()


if __name__ == "__main__":
    nums = [2, 3, 6, 7]
    target = 7
    combinations = combinations_of_sum_k(nums, target)
    print(f"Input: nums = {nums}, target = {target}")
    print("All combinations that sum to target:")
    for combo in combinations:
        print(combo)