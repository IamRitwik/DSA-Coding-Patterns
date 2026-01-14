
# Time - O(N)
# Space - O(M)
def longest_uniform_substring_after_replacements(s: str, k: int) -> int:
    freqs = {}
    highest_freq = 0
    max_length = 0
    left = right = 0

    while right < len(s):
        # update frequencies of character of right pointer in map
        freqs[s[right]] = freqs.get(s[right], 0) + 1
        # calculate highest frequency
        highest_freq = max(highest_freq, freqs[s[right]])

        # calculate number of characters to replace
        num_chars_to_replace = (right - left + 1) - highest_freq

        # if num_chars_to_replace <= k expand thw indow
        # if num_chars_to_replace > k slide the window

        # Invalid window (after shrinking) → right - left + 1 ≤ max_length
        # So max_length doesn't change
        if num_chars_to_replace > k:
            # remove character from left pointer from hash map
            freqs[s[left]] -= 1
            left += 1
        # Valid window → max_length increases or stays same
        max_length = max(max_length, right - left + 1)
        right += 1
    return max_length
    
"""
The algorithm automatically chooses the best option by tracking highest_freq.

Bottom Line
The algorithm implicitly decides to:

Keep: The character with highest_freq
Replace: All other characters (count = window_size - highest_freq)
This greedy approach is optimal because keeping the most frequent character minimizes 
the number of replacements needed!

"""
if __name__ == "__main__":
    s = "aabcdcca"
    k = 2

    print(longest_uniform_substring_after_replacements(s, k))
