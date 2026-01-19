from typing import List

def next_largest_number_to_the_right(nums: List[int]) -> List[int]:
    # Write your code here
    res = [0] * len(nums)
    stack = []

    # start from right most element
    for i in range(len(nums) - 1, -1, -1):
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        # current value's next largest no will be top of stack
        res[i] = stack[-1] if stack else -1
        stack.append(nums[i])
    return res

if __name__ == "__main__":
    nums = [5, 2, 4, 6, 1]
    print(next_largest_number_to_the_right(nums))