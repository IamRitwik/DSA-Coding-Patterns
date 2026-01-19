# Time: O(n)
# Space: O(n)
def valid_parenthesis_expression(s: str) -> bool:
    # Write your code here
    p_map = {'(': ')', '{': '}', '[': ']'}
    stack = []

    for c in s:
        # if current char is opening parenthesis
        if c in p_map:
            stack.append(c)
        else:
            if stack and p_map[stack[-1]] == c:
                stack.pop()
            else:
                return False
    return not stack



if __name__ == "__main__":
    s = '([]{})'
    print(valid_parenthesis_expression(s))