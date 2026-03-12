from typing import List

# Time Complexity: O(n)
# Space Complexity: O(1)
def jump_to_the_end(nums: List[int]) -> bool:
    destination = len(nums) - 1

    for i in range(len(nums) - 1, -1, -1):
        if i + nums[i] >= destination:
            destination = i
    
    return destination == 0


def main() -> None:
    # Simple reachable example
    nums = [2, 3, 1, 1, 4]
    expected = True
    result = jump_to_the_end(nums)
    print(f"jump_to_the_end({nums}) = {result} (expected {expected})")


if __name__ == "__main__":
    main()