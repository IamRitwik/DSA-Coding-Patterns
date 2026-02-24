from typing import Set

res = 0


def n_queens(n: int) -> int:
    global res
    res = 0  # reset result for each call
    dfs(0, set(), set(), set(), n)
    return res


def dfs(r: int, diag_set: Set[int], anti_diag_set: Set[int], col_set: Set[int], n: int) -> None:
    global res

    # termination condition - if we have reached end of the row
    if r == n:
        res += 1
        return

    for c in range(n):
        curr_diag = r - c
        curr_anti_diag = r + c

        # if queens in current diag, anti-diag, col skip
        if (c in col_set or curr_diag in diag_set or curr_anti_diag in anti_diag_set):
            continue

        # place the quuen
        col_set.add(c)
        diag_set.add(curr_diag)
        anti_diag_set.add(curr_anti_diag)

        # recursively continue to next row
        dfs(r + 1, diag_set, anti_diag_set, col_set, n)

        # backtrack
        col_set.remove(c)
        diag_set.remove(curr_diag)
        anti_diag_set.remove(curr_anti_diag)


if __name__ == "__main__":
    n = 4
    solutions = n_queens(n)
    print(f"Number of solutions for {n}-Queens:", solutions)