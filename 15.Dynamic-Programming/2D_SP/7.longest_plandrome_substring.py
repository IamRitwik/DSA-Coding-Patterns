def longest_palindrome_in_a_string(s: str) -> str:
    # Write your code here
    n = len(s)

    if n == 0:
        return ""
    
    dp = [[False] * n for _ in range(n)]

    max_len = 1
    start_index = 0

    # base case 1: single character
    for i in range(n):
        dp[i][i] = True

    # base case 2: substring of 2 characters
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            dp[i][i + 1] = True
            max_len = 2
            start_index = i
    # length = size of window
    # start = beiginning of window
    # end = start + length - 1
    for substring_len in range(3, n + 1):
        # i = start
        for i in range(n - substring_len + 1):
            # j = end
            j = i + substring_len - 1

            if s[i] == s[j] and dp[i + 1][j - 1]:
                dp[i][j] = True
                max_len = substring_len
                start_index = i
    
    return s[start_index: start_index + max_len]
