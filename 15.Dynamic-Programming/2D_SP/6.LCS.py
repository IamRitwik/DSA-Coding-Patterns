def longest_common_subsequence(s1: str, s2: str) -> int:

    # base case: populate last row with 0
    m, n = len(s1), len(s2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if s1[i] == s2[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    
    return dp[0][0]


def main() -> None:
    # Example test case
    s1 = "abcde"
    s2 = "ace"
    expected = 3  # LCS is "ace"
    result = longest_common_subsequence(s1, s2)
    print(f'LCS("{s1}", "{s2}") = {result} (expected {expected})')


if __name__ == "__main__":
    main()