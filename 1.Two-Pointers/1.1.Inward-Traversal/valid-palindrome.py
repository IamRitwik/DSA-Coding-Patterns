# Time - O(n)
# Space - O(1)
def is_palindrome_valid(s: str) -> bool:    
    # Write your code here
    #non_alpha_num_list = [char.lower() for char in s if char.isalnum()]
    #s = "".join(non_alpha_num_list)
    #print(s)

    left, right = 0, len(s)-1

    while left < right:

        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    s = "Was it a car or a cat I saw?"
    print(is_palindrome_valid(s))