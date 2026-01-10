# DSA Coding Patterns

A comprehensive collection of Data Structures and Algorithms implementations and coding patterns for technical interview preparation and competitive programming.

## 📚 About

This repository contains well-documented implementations of common data structures, algorithms, and coding patterns frequently encountered in technical interviews and competitive programming. Each implementation includes:

- Clear, readable code with comments
- Time and space complexity analysis
- Test cases and examples
- Step-by-step explanations where applicable

## 📊 Problems Quick Reference

| # | Problem Name | Pattern | Difficulty | Quick Interview Tip |
|---|-------------|---------|------------|---------------------|
| 1 | [Pair Sum in Sorted Array](1.Two-Pointers/1.1.Inward-Traversal/pair-sum-sorted.py) | Two Pointers (Inward) | Easy | **Sorted array + target sum** → Use two pointers from both ends, move based on sum comparison |
| 2 | [Valid Palindrome](1.Two-Pointers/1.1.Inward-Traversal/valid-palindrome.py) | Two Pointers (Inward) | Easy | **Palindrome check** → Use two pointers from both ends, skip non-alphanumeric chars, compare lowercase |
| 3 | [Triplet Sum](1.Two-Pointers/1.1.Inward-Traversal/triplet-sum.py) | Two Pointers (Inward) | Medium | **Find triplets summing to 0** → Sort array, fix first element, use two pointers for remaining pairs. Skip duplicates! |
| 4 | [Container With Most Water](1.Two-Pointers/1.1.Inward-Traversal/largest_container.py) | Two Pointers (Inward) | Medium | **Maximize area between lines** → Start with widest container, move pointer with shorter height inward |
| 5 | [Move Zeros](1.Two-Pointers/1.2.Unidirectional-Traversal/move_zeros.py) | Two Pointers (Unidirectional) | Easy | **Move elements to end** → Use slow pointer for position, fast pointer to scan, swap non-zero elements |
| 6 | [Next Lexicographical Sequence](1.Two-Pointers/1.3.Staged-Traversal/next_lexicographical_sequence.py) | Two Pointers (Staged Traversal) | Medium | **Next permutation** → Find rightmost pivot (a[i] < a[i+1]), swap with next larger element from right, then reverse the suffix |
| 7 | [Two Sum (Unsorted)](2.HashMap-Sets/2.1.Maps/2sum.py) | HashMaps & Sets | Easy | **Unsorted array + target sum** → Use a hash map to store seen numbers and their indices; check for `target - current` in the map |
| 8 | [Valid Sudoku](2.HashMap-Sets/2.2.Sets/verify_sudoku_board.py) | HashMaps & Sets | Medium | **3x3 Subgrids** → Use sets for rows, columns, and subgrids; map `(r, c)` to subgrid index using `(r // 3, c // 3)` |
| 9 | [Set Matrix Zeros](2.HashMap-Sets/2.2.Sets/set_matrix_zeros.py) | HashMaps & Sets | Medium | **Flagging rows/cols** → Track row and column indices that contain zeros in sets, then update the matrix in a second pass |
| 10 | [Longest Consecutive Sequence](2.HashMap-Sets/2.2.Sets/longest_chain_consecutive_nums.py) | HashMaps & Sets | Medium | **Longest streak** → Use a set to find the start of each sequence (where `num - 1` is missing) and count upwards |
| 11 | [Geometric Triplet Sequence](2.HashMap-Sets/2.1.Maps/geometric_triplet_sequence.py) | HashMaps & Sets | Medium | **Geometric triplets** → Use two frequency maps (left and right) to count triplets where `x/r` and `x*r` exist |
| 12 | [Linked List Reversal](3.LinkedLists/3.1.Resturcturing/reverse.py) | Linked Lists | Easy | **Reverse Linked List** → Use three pointers (`prev`, `curr`, `next`) to reverse node connections in-place |
| 13 | [Remove Kth Last Node](3.LinkedLists/3.1.Resturcturing/remove_kth_node.py) | Linked Lists (Two Pointers) | Medium | **Two-pointer approach** → Use a leader pointer with a k-node head start to find the node before target |
| 14 | [Intersection of Two Linked Lists](3.LinkedLists/3.2.Traversal/intersection.py) | Linked Lists (Two Pointers) | Easy | **Find intersection point** → Use two pointers, move each to the other list's head after reaching null to equalize path lengths |
| 15 | [LRU Cache](3.LinkedLists/3.3.DoublyLinkedList/LRU_cache.py) | Doubly Linked Lists & HashMaps | Medium | **O(1) Get/Put** → Combine a doubly linked list (for ordering) and a hash map (for O(1) access) |
| 16 | [Palindrome Linked List](3.LinkedLists/3.2.Traversal/palindrome_linked_list.py) | Linked Lists (Two Pointers) | Easy | **Palindrome check** → Find middle (fast/slow), reverse second half, compare with first half |
| 17 | [Flatten Multi-Level Linked List](3.LinkedLists/3.1.Resturcturing/flatten-multi-level-list.py) | Linked Lists (Restructuring) | Medium | **Flatten multi-level list** -> Append each child branch to the tail of the main list for a linear result |

> **Note**: This table will be updated as more problems are added to the repository.



## 📝 License

This project is open source and available for educational purposes.

## 🙏 Acknowledgments

- Inspired by common coding interview patterns
- Built for learning and interview preparation


