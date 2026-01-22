from collections import deque
from typing import List

def maximums_of_sliding_window(nums: List[int], k: int) -> List[int]:
    # Write your code here
    res = []
    dq = deque()
    left, right = 0, 0

    while right < len(nums):
        # 1. ensure deque maintains monotonic decreasing order
        # by removing candidates <= current value
        while dq and dq[-1][0] <= nums[right]:
            dq.pop()
        
        # 2. add current candidate
        dq.append((nums[right], right))

        # if window of length k, record maximum
        if right - left + 1 == k:
            # 3. remove outdated values
            if dq and dq[0][1] < left:
                dq.popleft()
            # maximum of window is left most value
            res.append(dq[0][0])
            left += 1
        right += 1
    return res

if __name__ == "__main__":
    nums = [3, 2, 4, 1, 2, 1, 1]
    k = 4

    print(maximums_of_sliding_window(nums, k))