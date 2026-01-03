# Time - O(n)
# Space - O(1)
def shift_zeros_to_the_end(nums: List[int]) -> None:

    left = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1


if __name__ == "__main__":
    nums = [0,1,0,3,12]
    shift_zeros_to_the_end(nums)
    print(nums)