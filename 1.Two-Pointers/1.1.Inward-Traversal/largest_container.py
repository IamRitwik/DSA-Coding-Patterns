from typing import List

# Time - O(n^2)
# Space - O(1)
def largest_container_brute_force(heights: List[int]) -> int:
    # Write your code here
    n = len(heights)
    max_water = 0
    for i in range(n):
        for j in range(i+1, n):
            water = min(heights[i], heights[j])*(j-i)
            max_water = max(max_water, water)
    return max_water

# Time - O(n)
# Space - O(1)
def largest_container(heights: List[int]) -> int:
    # Write your code here
    max_area = 0
    left, right = 0, len(heights) - 1

    while left < right:
        water = min(heights[left], heights[right]) * (right - left)
        max_area = max(water, max_area)

        if heights[left] < heights[right]:
            left += 1
        elif heights[left] > heights[right]:
            right -= 1
        else:
            left += 1
            right -= 1
    return max_area

if __name__ == "__main__":
    heights = [0,2,0,3,1,0,1,3,2,1]
    max_water = largest_container_brute_force(heights)
    print(max_water)

    max_water = largest_container(heights)
    print(max_water)