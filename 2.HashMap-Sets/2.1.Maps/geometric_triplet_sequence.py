from collections import defaultdict
from typing import List

# Time - O(n)
# Space - O(n)
def geometric_sequence_triplets(nums: List[int], r: int) -> int:
    # Write your code here
    left_map = defaultdict(int)
    right_map = defaultdict(int)
    count = 0

    for x in nums:
        right_map[x] += 1

    for x in nums:
        right_map[x] -= 1
        if x % r == 0:
            count += left_map[x // r] * right_map[x * r]
        left_map[x] += 1

    return count


if __name__ == "__main__":
    nums = [2, 1, 2, 4, 8, 8]
    r = 2
    print(geometric_sequence_triplets(nums, r))