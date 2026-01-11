# Time - O(N)
# Space - O(M)
def longest_substring_with_unique_chars(s: str) -> int:
   # Write your code here
   max_len = 0
   hash_set = set()
   left = right = 0
   while right < len(s):
        # duplicate found
        while s[right] in hash_set:
            hash_set.remove(s[left])
            # shrink window
            left += 1
        max_len = max(max_len, right - left + 1)
        hash_set.add(s[right])
        # expand window
        right += 1

   return max_len 



if __name__ == "__main__":
   s = "abcba"
   print(longest_substring_with_unique_chars(s))