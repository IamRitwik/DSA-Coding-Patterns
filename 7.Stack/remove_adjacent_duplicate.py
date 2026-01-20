def repeated_removal_of_adjacent_duplicates(s: str) -> str:
    # Write your code here
    stack = []

    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return ''.join(stack)


if __name__ == "__main__":
    s = 'aacabba'
    print(repeated_removal_of_adjacent_duplicates(s))