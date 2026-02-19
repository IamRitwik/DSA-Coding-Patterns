from typing import List, Set


# Time complexity:
# - There are n! permutations for an input of size n.
# - For each complete permutation we spend O(n) work to build/copy it into the result.
# - The backtracking tree has branching factor up to n and depth n, which yields O(n * n!) 
# total operations.
# Overall time complexity: O(n * n!).
#
# Space complexity:
# - The recursion stack can go as deep as n, and the current candidate list and used set 
# each hold at most n elements.
# - Ignoring the output, the extra auxiliary space is O(n).
# - The output list itself stores all permutations, which takes O(n × n!) space.
# Overall space complexity: O(n × n!) including the output, and O(n) auxiliary.
def find_all_permutations(nums: List[int]) -> List[List[int]]:
    res: List[List[int]] = []
    backtrack(nums, [], set(), res)
    return res


def backtrack(nums: List[int], candidate: List[int], used: Set[int], res: List[List[int]]) -> None:
    # if current candidate is complete permutation, add to the result
    if len(candidate) == len(nums):
        res.append(candidate[:])
        return

    for num in nums:
        if num not in used:
            # add num to current permutation and set
            candidate.append(num)
            used.add(num)

            # explore branches recursively
            backtrack(nums, candidate, used, res)

            # backtrack by reversing the changes made
            candidate.pop()
            used.remove(num)


if __name__ == "__main__":
    nums = [4, 5, 6]
    permutations = find_all_permutations(nums)
    print(f"Input: {nums}")
    print("All permutations:")
    for p in permutations:
        print(p)

