import heapq
import random
from typing import List


def kth_largest_integer(nums: List[int], k: int) -> int:
    # Time Complexity: O(n log k)
    # Space Complexity: O(k)
    min_heap = []

    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)

    return min_heap[0]

# Time Complexity: O(n) on average, O(n^2) worst case
# Space Complexity: O(log n) for recursion stack, worst O(n)
def kth_largest_integer_v2(nums: List[int], k: int) -> int:
    return quickselect(nums, 0, len(nums) - 1, k)

def quickselect(nums: List[int], left: int, right: int, k: int) -> int:
    n = len(nums)

    if left >= right:
        return nums[left]

    random_index = random.randint(left, right)
    nums[random_index], nums[right] = nums[right], nums[random_index]

    pivot_index = partition(nums, left, right)

    if pivot_index < n - k:
        return quickselect(nums, pivot_index + 1, right, k)
    elif pivot_index > n - k:
        return quickselect(nums, left, pivot_index - 1, k)
    else:
        return nums[pivot_index]

def partition(nums: List[int], left: int, right: int) -> int:
    pivot = nums[right]

    lo = left

    for i in range(left, right):
        if nums[i] < pivot:
            nums[lo], nums[i] = nums[i], nums[lo]
            lo += 1
    
    nums[lo], nums[right] = nums[right], nums[lo]

    return lo


if __name__ == "__main__":
    # test case for kth_largest_integer
    nums = [3, 2, 1, 5, 6, 4]
    k = 3
    result = kth_largest_integer_v2(nums, k)
    print(f"{k}-th largest element in {nums} is: {result}")