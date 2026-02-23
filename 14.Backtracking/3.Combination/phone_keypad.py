from typing import List, Dict


# Time complexity:
# - Let n be the number of digits.
# - Each digit maps to 3–4 letters, so the branching factor is up to 4.
# - The total number of combinations is at most 4^n, and building each string costs O(n).
# Overall time complexity: O(n * 4^n).
#
# Space complexity:
# - The recursion depth and current `combination` list length are at most n → O(n) auxiliary space.
# - The result list stores all generated combinations, which is O(n * 4^n) characters total.
# Overall space complexity: O(n * 4^n) including output, and O(n) auxiliary.
def phone_keypad_combinations(digits: str) -> List[str]:
    keypad_map = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }

    res: List[str] = []
    if digits:
        backtrack(0, [], digits, keypad_map, res)
    return res


def backtrack(i: int, combination: List[str], digits: str, keypad_map: Dict[str, str], res: List[str]) -> None:
    
    if len(combination) == len(digits):
        res.append("".join(combination))
        return

    for letter in keypad_map[digits[i]]:

        combination.append(letter)

        backtrack(i + 1, combination, digits, keypad_map, res)

        combination.pop()


if __name__ == "__main__":
    digits = "23"
    combinations = phone_keypad_combinations(digits)
    print(f"Input digits: {digits}")
    print("All possible letter combinations:")
    for combo in combinations:
        print(combo)