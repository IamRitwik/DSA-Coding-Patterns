def evaluate_expression(s: str) -> int:
    # Write your code here
    stack = []

    curr_num, sign, res = 0, 1, 0

    for c in s:
        if c.isdigit():
            curr_num = curr_num * 10 + int(c)
        # check if c is operator
        elif c == '+' or c == '-':
            res += curr_num * sign
            sign = -1 if c == '-' else 1
            curr_num = 0
        
        elif c == '(':
            # save the res and sign by pushing them 
            # onto stack then reset their values to start
            stack.append(res)
            stack.append(sign)
            res, sign = 0, 1

        elif c == ')':
            res += sign * curr_num
            res *= stack.pop()
            res += stack.pop()
            curr_num = 0
    return res + curr_num * sign

if __name__ == "__main__":
    s = "18-(7+(2-4))"
    print(evaluate_expression(s))