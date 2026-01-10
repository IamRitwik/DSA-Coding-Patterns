# Time - O(log(N))
# Space - O(1)
def happy_number(n: int) -> bool:
    # Write your code here
    slow = fast = n
    while True:
        slow = get_next_num(slow)
        fast = get_next_num(get_next_num(fast))

        if fast == 1:
            return True
        elif slow == fast:
            return False

def get_next_num(x: int) -> int:
    next_num = 0

    while x > 0:
        digit = x % 10
        x = x // 10
        next_num += digit ** 2
    return next_num


if __name__ == "__main__":
    print(happy_number(23))
    print(happy_number(100))
    print(happy_number(116))