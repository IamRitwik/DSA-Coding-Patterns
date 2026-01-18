from typing import List
import random

# Time: O(logn)
# Space: O(n)
class WeightedRandomSelection:
    def __init__(self, weights: List[int]):
        self.prefix_sums = [weights[0]]

        for i in range(1, len(weights)):
            self.prefix_sums.append(self.prefix_sums[-1] + weights[i])

    # Lower boundary binary search
    def select(self) -> int:
        target = random.randint(1, self.prefix_sums[-1])

        left, right = 0, len(self.prefix_sums) 

        while left < right:
            mid = (left + right) // 2

            if self.prefix_sums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        return left