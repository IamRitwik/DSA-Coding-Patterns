from typing import List

# Time: O(log(min(m,n)))
# Space: O(1)
def find_the_median_from_two_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    # optimization for binary search
    if len(nums2) < len(nums1):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    half_total_len = (m + n) // 2
    left, right = 0, m - 1

    while True:
        L1_index = (left + right) // 2
        
        # Calculate how many elements we need from nums2
        # total_left_needed (hal_total_len) - elements_from_nums1 (L1_index + 1) - 1 (for 0-based index)
        L2_index = half_total_len - (L1_index + 1) - 1

        # set to -inf or +inf if out of bounds
        L1 = float('-inf') if L1_index < 0 else nums1[L1_index]
        R1 = float('inf') if L1_index >= m - 1 else nums1[L1_index + 1]
        L2 = float('-inf') if L2_index < 0 else nums2[L2_index]
        R2 = float('inf') if L2_index >= n - 1 else nums2[L2_index + 1]

        if L1 > R2:
            right = L1_index - 1
        elif L2 > R1:
            left = L1_index + 1
        else:
            if (m + n) % 2 == 0:
                return (max(L1, L2) + min(R1, R2)) / 2.0
            else:
                return min(R1, R2)



if __name__ == "__main__":
    nums1 = [0, 2, 5, 6, 8]
    nums2 = [1, 3, 7]
    print(find_the_median_from_two_sorted_arrays(nums1, nums2))

    nums1 = [0, 2, 5, 6, 8]
    nums2 = [1, 3, 7, 9]
    print(find_the_median_from_two_sorted_arrays(nums1, nums2))