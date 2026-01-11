# Time - O(N)
# Space - O(1)
def substring_anagrams(s: str, t: str) -> int:
    # Write your code here.
    len_s, len_t = len(s), len(t)
    if len_t > len_s:
        return 0
    count = 0
    expected_freq, window_freq = [0]*26, [0]*26

    # populate the expected frequency array
    for c in t:
        expected_freq[ord(c) - ord('a')] += 1
    #print(expected_freq)

    left = right = 0
    while right < len_s:
        # add chracter of right pointer to window_freq
        window_freq[ord(s[right]) - ord('a')] += 1
        # fixed length window
        # if the window reached fixed length, we advance left as well as right 
        # pointer to slide the window
        if right - left + 1 == len_t:
            if window_freq == expected_freq:
                count += 1
            # remove the character at the left pointer from window_freq
            window_freq[ord(s[left]) - ord('a')] -= 1
            left += 1
        right += 1
    return count




if __name__ == "__main__":
    s = "caabab"
    t = "aba"
    print(substring_anagrams(s, t))