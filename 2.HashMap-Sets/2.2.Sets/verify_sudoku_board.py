from typing import List

def verify_sudoku_board(board: List[List[str]]) -> bool:
    # Write your code here
    row_sets = [set() for _ in range(9)]
    col_sets = [set() for _ in range(9)]
    subgrid_sets = [[set() for _ in range(3)] for _ in range(3)]

    for r in range(9):
        for c in range(9):
            num = board[r][c]

            if num == ".":
                continue

            # check if num has been seen in row, col, subgrid
            if num in row_sets[r]:
                return False
            if num in col_sets[c]:
                return False
            if num in subgrid_sets[r // 3][c // 3]:
                return False
            
            # if above checks pass add the value in 
            # corresponding hashsets
            row_sets[r].add(num)
            col_sets[c].add(num)
            subgrid_sets[r // 3][c //3 ].add(num)

    return True


if __name__ == "__main__":
    board = [
        ["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","8",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]
    ]

    print(verify_sudoku_board(board))


    board_2 = [ ["1","2",".",".","3",".",".",".","."],
                ["4",".",".","5",".",".",".",".","."],
                [".","9","1",".",".",".",".",".","3"],
                ["5",".",".",".","6",".",".",".","4"],
                [".",".",".","8",".","3",".",".","5"],
                ["7",".",".",".","2",".",".",".","6"],
                [".",".",".",".",".",".","2",".","."],
                [".",".",".","4","1","9",".",".","8"],
                [".",".",".",".","8",".",".","7","9"] ]
    
    print(verify_sudoku_board(board_2))