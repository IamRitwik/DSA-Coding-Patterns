"""
Next Lexicographical Sequence (Next Permutation)
Pattern: Two Pointers - Staged Traversal
Difficulty: Medium

Problem:
Given a string/array, rearrange it to the next lexicographically greater permutation.
If it's already the last permutation, return the first (smallest) permutation.

Algorithm (4 Steps):
1. Find Pivot: Scan right-to-left to find first position where arr[i] < arr[i+1]
2. Find Successor: From right, find smallest element > pivot
3. Swap: Swap pivot with successor
4. Reverse Suffix: Reverse everything after pivot position (using two pointers)

Time Complexity: O(n) - each step scans at most n elements
Space Complexity: O(1) for in-place version, O(n) for string version (due to list conversion)
"""

def next_permutation_string(s):
    """
    String version - returns new string
    Example: 'abcd' -> 'abdc'
    """
    chars = list(s)
    n = len(chars)
    
    # Step 1: Find pivot (rightmost position where chars[i] < chars[i+1])
    # This identifies where we need to make a change
    pivot = -1
    for i in range(n - 2, -1, -1):
        if chars[i] < chars[i + 1]:
            pivot = i
            break
    
    # If no pivot found, we're at the last permutation
    # Return the first permutation (sorted in ascending order)
    if pivot == -1:
        return ''.join(sorted(chars))
    
    # Step 2: Find successor (smallest element > pivot, searching from right)
    # This ensures we get the NEXT permutation, not just any larger one
    for i in range(n - 1, pivot, -1):
        if chars[i] > chars[pivot]:
            # Step 3: Swap pivot with successor
            chars[pivot], chars[i] = chars[i], chars[pivot]
            break
    
    # Step 4: Reverse suffix (TWO POINTER PATTERN - Inward Traversal)
    # After swapping, the suffix is in descending order
    # We reverse it to get the smallest possible arrangement
    left, right = pivot + 1, n - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    
    return ''.join(chars)


def next_permutation_inplace(nums):
    """
    LeetCode #31 version - modifies array in-place
    Example: [1,2,3] -> [1,3,2]
    
    Args:
        nums: List[int] - array to modify in-place
    Returns:
        None - modifies nums in-place
    """
    n = len(nums)
    
    # Step 1: Find pivot
    pivot = -1
    for i in range(n - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            pivot = i
            break
    
    # If no pivot, reverse entire array (last -> first permutation)
    if pivot == -1:
        nums.reverse()
        return
    
    # Step 2: Find successor
    for i in range(n - 1, pivot, -1):
        if nums[i] > nums[pivot]:
            # Step 3: Swap
            nums[pivot], nums[i] = nums[i], nums[pivot]
            break
    
    # Step 4: Reverse suffix (TWO POINTERS)
    left, right = pivot + 1, n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1


# Test cases
if __name__ == "__main__":
    print("=== String Version Tests ===")
    
    # Test 1: Normal case
    test1 = "abcd"
    result1 = next_permutation_string(test1)
    print(f"Input: '{test1}' -> Output: '{result1}'")
    print(f"Expected: 'abdc' | Pass: {result1 == 'abdc'}\n")
    
    # Test 2: Last permutation (should wrap to first)
    test2 = "dcba"
    result2 = next_permutation_string(test2)
    print(f"Input: '{test2}' -> Output: '{result2}'")
    print(f"Expected: 'abcd' | Pass: {result2 == 'abcd'}\n")
    
    # Test 3: Another example
    test3 = "acbd"
    result3 = next_permutation_string(test3)
    print(f"Input: '{test3}' -> Output: '{result3}'")
    print(f"Expected: 'acdb' | Pass: {result3 == 'acdb'}\n")
    
    print("=== Array Version Tests (LeetCode #31) ===")
    
    # Test 4: Normal case
    test4 = [1, 2, 3]
    next_permutation_inplace(test4)
    print(f"Input: [1,2,3] -> Output: {test4}")
    print(f"Expected: [1,3,2] | Pass: {test4 == [1, 3, 2]}\n")
    
    # Test 5: Last permutation
    test5 = [3, 2, 1]
    next_permutation_inplace(test5)
    print(f"Input: [3,2,1] -> Output: {test5}")
    print(f"Expected: [1,2,3] | Pass: {test5 == [1, 2, 3]}\n")
    
    # Test 6: Complex example
    test6 = [1, 3, 2]
    next_permutation_inplace(test6)
    print(f"Input: [1,3,2] -> Output: {test6}")
    print(f"Expected: [2,1,3] | Pass: {test6 == [2, 1, 3]}\n")
    
    # Test 7: Single element
    test7 = [1]
    next_permutation_inplace(test7)
    print(f"Input: [1] -> Output: {test7}")
    print(f"Expected: [1] | Pass: {test7 == [1]}\n")