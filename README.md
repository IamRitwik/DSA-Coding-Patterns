# DSA Coding Patterns

A comprehensive collection of Data Structures and Algorithms implementations and coding patterns for technical interview preparation and competitive programming.

## 📚 About

This repository contains well-documented implementations of common data structures, algorithms, and coding patterns frequently encountered in technical interviews and competitive programming. Each implementation includes:


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
| 18 | [Linked List Loop](4.Fast-Slow-Pointer/linked-list-loop.py) | Fast & Slow Pointers | Easy | **Detect cycle in linked list** → Fast moves 2x faster; if pointers meet, a cycle exists |
| 19 | [Midpoint of Linked List](4.Fast-Slow-Pointer/mid-point.py) | Fast & Slow Pointers | Easy | **Find the middle node** → Fast moves 2 steps, slow moves 1; slow is at mid when fast reaches end |
| 20 | [Happy Number](4.Fast-Slow-Pointer/happy_number.py) | Fast & Slow Pointers | Easy | **Cycle detection in sequences** → Use fast/slow pointers on the sequence of digit square sums |
| 21 | [Substring Anagrams](5.Sliding-Window/5.1.Fixed-Window/substring-anagrams.py) | Sliding Window (Fixed Window) | Medium | **Match Anagrams** → Use fixed-size window & frequency arrays; compare window counts with pattern counts |
| 22 | [Longest Substring Without Repeating Characters](5.Sliding-Window/152.Dynamic-Window/longest_sub-string_without_repeating_chars.py) | Sliding Window (Dynamic Window) | Medium | **No duplicate characters** → Use dynamic window with hash set; shrink from left when duplicate found, expand from right |
| 23 | [Longest Uniform Substring After Replacement](5.Sliding-Window/152.Dynamic-Window/longest_uniform_sub-string_after_replacement.py) | Sliding Window (Dynamic Window) | Medium | **K replacements allowed** → Track highest frequency character; slide window when `(window_size - highest_freq) > k` |
| 24 | [Find Insertion Index](6.Binary-Search/6.1.Sorted-Arrays/find_insertion_index.py) | Binary Search (Lower Bound) | Easy | **Find insertion position** → Use `left < right` with search space `[0, N]`; update `right = mid` (not `mid - 1`) to find lower bound |
| 25 | [First and Last Occurrences of a Number](6.Binary-Search/6.1.Sorted-Arrays/first_last_occurrences_of_no.py) | Binary Search (Lower/Upper Bound) | Medium | **Find range of target** → Use lower bound to find first occurrence, upper bound - 1 to find last occurrence; check if target exists |
| 26 | [Cutting Wood](6.Binary-Search/6.2.Non-Intuitive-Search-Space/cutting-wood.py) | Binary Search (Upper Bound / Answer) | Medium | **Maximize result** → Binary search on answer range `[0, max(H)]`; find last `mid` where condition holds (upper bound logic) |
| 27 | [Local Maxima in Array](6.Binary-Search/6.2.Non-Intuitive-Search-Space/local_maxima_in_array.py) | Binary Search (Non-Intuitive Search Space) | Medium | **Find local maxima** → Use binary search to find the index of the local maxima in the array |
| 28 | [Weighted Random Selection](6.Binary-Search/6.2.Non-Intuitive-Search-Space/weighted_random_selection.py) | Binary Search (Non-Intuitive Search Space) | Medium | **Weighted random selection** → Use binary search to select an element from an array based on its weight |
| 29 | [Search in Rotated Sorted Array](6.Binary-Search/6.3.Rotated-Sorted-Arrays/search_in_rotated_sorted_array.py) | Binary Search (Rotated Sorted Arrays) | Medium | **Rotated sorted array** → Identify which half is sorted; check if target is within the sorted half's range to decide search direction |
| 30 | [Median of Two Sorted Arrays](6.Binary-Search/6.4.Multiple-Arrays/median-of-2-sorted-arrays.py) | Binary Search (Multiple Arrays) | Hard | **Partitioning** → Binary search on the smaller array to partition both arrays such that left halves <= right halves |
| 31 | [Search a 2D Matrix](6.Binary-Search/6.5.Matrix/matrix-search.py) | Binary Search (2D Matrix) | Medium | **Treat as 1D array** → Map 2D indices (row, col) to 1D index `i` using `row = i // n`, `col = i % n` |
| 32 | [Valid Parenthesis](7.Stack/valid_parenthesis.py) | Stack | Easy | **Balanced Parentheses** → Push opening brackets to stack; pop and check for match when closing bracket appears |
| 33 | [Next Largest Number to the Right](7.Stack/next_largest_no_to_right.py) | Monotonic Stack | Medium | **Monotonic Stack** → Iterate backwards; pop smaller elements from stack top to find next greater; push current |


> **Note**: This table will be updated as more problems are added to the repository.



## 📝 License

This project is open source and available for educational purposes.

## 🙏 Acknowledgments

- Inspired by common coding interview patterns
- Built for learning and interview preparation


