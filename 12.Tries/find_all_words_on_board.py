from typing import List

class TrieNode:
    def __init__(self) -> None:
        self.children = {}
        self.word = None

def find_all_words_on_a_board(board: List[List[str]], words: List[str]) -> List[str]:
    """
    Find all words from the given list that exist on the board.
    
    Time Complexity: O(M * N * 4^L + W * L)
    - M * N: dimensions of the board
    - L: maximum length of a word
    - 4^L: worst case DFS exploration (4 directions, L depth)
    - W * L: building the Trie (W words, L average length)
    
    Space Complexity: O(W * L + L)
    - W * L: Trie storage for all words
    - L: recursion stack depth for DFS
    """
    # Build Trie from all words
    root = TrieNode()

    # Insert every word into trie
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.word = word
    res = []

    # DFS
    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] in root.children:
                dfs(board, r, c, root.children[board[r][c]], res)
    return res

def dfs(board: List[List[str]], r: int, c: int, node: TrieNode, res: List[str]) -> None:
    """
    Depth-first search to find words on the board using Trie.
    
    Time Complexity: O(4^L) where L is the length of the word
    - At each cell, we explore up to 4 directions
    - Maximum depth is L (length of longest word)
    
    Space Complexity: O(L) for recursion stack
    """
    # If the current word represents end of word, add to result
    if node.word:
        res.append(node.word)
        node.word = None
    
    temp = board[r][c]

    # mark the current cell visited
    board[r][c] = '#'

    # explore all adjacent cells
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for d in dirs:
        next_r, next_c = r + d[0], c + d[1]
        if (is_within_bounds(next_r, next_c, board) and board[next_r][next_c] in node.children):
            dfs(
                board, next_r, next_c,
                node.children[board[next_r][next_c]],
                res
            )
    # Backtrack
    board[r][c] = temp

def is_within_bounds(r: int, c: int, board: List[List[str]]) -> bool:
    """
    Check if the given position is within board boundaries.
    
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    return 0 <= r < len(board) and 0 <= c < len(board[0])

def main():
    # Test Case 1: Classic example with multiple words
    board1 = [
        ['o', 'a', 'a', 'n'],
        ['e', 't', 'a', 'e'],
        ['i', 'h', 'k', 'r'],
        ['i', 'f', 'l', 'v']
    ]
    words1 = ["oath", "pea", "eat", "rain"]
    result1 = find_all_words_on_a_board(board1, words1)
    print("Test Case 1:")
    print(f"Board: {board1}")
    print(f"Words to find: {words1}")
    print(f"Found words: {result1}")
    print(f"Expected: ['oath', 'eat'] (order may vary)")
    print()

    # Test Case 2: Single character words
    board2 = [
        ['a', 'b'],
        ['c', 'd']
    ]
    words2 = ["a", "b", "c", "d", "e"]
    result2 = find_all_words_on_a_board(board2, words2)
    print("Test Case 2:")
    print(f"Board: {board2}")
    print(f"Words to find: {words2}")
    print(f"Found words: {result2}")
    print(f"Expected: ['a', 'b', 'c', 'd'] (order may vary)")
    print()

    # Test Case 3: Words with path traversal
    board3 = [
        ['a', 'b', 'c'],
        ['a', 'e', 'd'],
        ['a', 'f', 'g']
    ]
    words3 = ["abcdefg", "gfedcba", "eaabcdgf", "befa"]
    result3 = find_all_words_on_a_board(board3, words3)
    print("Test Case 3:")
    print(f"Board: {board3}")
    print(f"Words to find: {words3}")
    print(f"Found words: {result3}")
    print()

    # Test Case 4: No words found
    board4 = [
        ['a', 'a'],
        ['a', 'a']
    ]
    words4 = ["b", "c", "ab"]
    result4 = find_all_words_on_a_board(board4, words4)
    print("Test Case 4:")
    print(f"Board: {board4}")
    print(f"Words to find: {words4}")
    print(f"Found words: {result4}")
    print(f"Expected: []")
    print()

if __name__ == "__main__":
    main()