from typing import List

def product_array_without_current_element(nums: List[int]) -> List[int]:
    # Write your code here
    n = len(nums)
    res = [1] * n

    for i in range(1, n):
        res[i] = res[i-1] * nums[i-1]
    
    right_product = 1
    for i in range(n-1, -1, -1):
        res[i] = res[i] * right_product
        right_product = right_product * nums[i]
    
    return res


if __name__ == "__main__":
    nums = [2, 3, 1, 4, 5]
    print(product_array_without_current_element(nums))