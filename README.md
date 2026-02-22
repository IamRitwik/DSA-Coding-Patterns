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
| 27 | [Local Maxima in Array](6.Binary-Search/6.2.Non-Intuitive-Search-Space/local_maxima_in_array.py) | Binary Search (Non-Intuitive Search Space) | Medium | **Find local maxima** → Compare `arr[mid]` with neighbors; if `arr[mid] > arr[mid+1]`, peak is on left (including mid), else on right |
| 28 | [Weighted Random Selection](6.Binary-Search/6.2.Non-Intuitive-Search-Space/weighted_random_selection.py) | Binary Search (Non-Intuitive Search Space) | Medium | **Weighted random selection** → Build prefix sum array; generate random in `[0, total_sum)`, binary search for insertion point |
| 29 | [Search in Rotated Sorted Array](6.Binary-Search/6.3.Partially-Sorted-Array/search_in_rotated_sorted_array.py) | Binary Search (Rotated Sorted Arrays) | Medium | **Rotated sorted array** → Identify which half is sorted; check if target is within the sorted half's range to decide search direction |
| 30 | [Median of Two Sorted Arrays](6.Binary-Search/6.4.Multiple-Arrays/median-of-2-sorted-arrays.py) | Binary Search (Multiple Arrays) | Hard | **Partitioning** → Binary search on smaller array; ensure `len(left_half) = len(right_half)` and `max(left) <= min(right)` |
| 31 | [Search a 2D Matrix](6.Binary-Search/6.5.Matrix/matrix-search.py) | Binary Search (2D Matrix) | Medium | **Treat as 1D array** → Map 2D indices to 1D: `row = mid // cols`, `col = mid % cols`; search space is `[0, rows*cols)` |
| 32 | [Valid Parenthesis](7.Stack/valid_parenthesis.py) | Stack | Easy | **Balanced Parentheses** → Push opening brackets to stack; pop and check for match when closing bracket appears |
| 33 | [Next Largest Number to the Right](7.Stack/next_largest_no_to_right.py) | Monotonic Stack | Medium | **Monotonic Stack** → Iterate backwards; pop smaller elements from stack top to find next greater; push current |
| 34 | [Basic Calculator (Evaluate Expression)](7.Stack/evaluate_expression.py) | Stack | Hard | **Expression with parentheses** → Use stack to save context (result & sign) when entering `(`, restore when exiting `)` |
| 35 | [Remove Adjacent Duplicates](7.Stack/remove_adjacent_duplicate.py) | Stack | Easy | **Remove adjacent duplicates** → Push to stack if different from top; pop if same as top (cancel out duplicates) |
| 36 | [Queue Using Stacks](7.Stack/queue_using_stack.py) | Stack | Medium | **Implement queue with stacks** → Use two stacks: one for enqueue (O(1)), one for dequeue; transfer elements lazily for amortized O(1) operations |
| 37 | [Sliding Window Maximum](7.Stack/sliding_window_maximum.py) | Monotonic Deque | Hard | **Find max in each window** → Use monotonic decreasing deque to track potential maximums; remove smaller elements from back, outdated from front |
| 38 | [Merge K Sorted Lists](8.Heap/Sorting/merge-k-sorted-lists.py) | Heap (Sorting) | Hard | **Merge multiple sorted lists** → Use min heap to track smallest element from each list; pop smallest, push its next node. O(N log k) time |
| 39 | [K Most Frequent Strings (Max Heap)](8.Heap/Finding_In_Sorted_Order/k-most-frequent-strings-max-heap.py) | Heap (Finding in Sorted Order) | Medium | **Top K frequent elements** → Build max heap with custom comparator (freq desc, then string asc); pop k times. O(n + k log n) time |
| 40 | [K Most Frequent Strings (Min Heap)](8.Heap/Finding_In_Sorted_Order/k-most-frequent-strings-min-heap.py) | Heap (Finding in Sorted Order) | Medium | **Top K with size-k heap** → Maintain min heap of size k; push all elements, pop when size > k. O(n log k) time, O(k) space |
| 41 | [Median of Stream](8.Heap/Finding_In_Sorted_Order/median_of_stream.py) | Heap (Two Heaps) | Hard | **Running median** → Use max heap (left half) and min heap (right half); balance heaps to keep sizes equal or left_size = right_size + 1 |
| 42 | [Sort K-Sorted Array](8.Heap/Sorting/sort_k_sorted_array.py) | Heap (Sorting) | Medium | **Nearly sorted array** → Use min heap of size k+1; smallest element in array must be within first k+1 positions. O(n log k) time |
| 43 | [Merge Intervals](9.Merge-Intervals/merge-overlap-intervals.py) | Merge Intervals | Medium | **Sort & Merge** → Sort by start time; merge if `current.end >= next.start` |
| 44 | [Interval List Intersections](9.Merge-Intervals/identify-interval-overlaps.py) | Merge Intervals (Two Pointers) | Medium | **Find common time** → Use two pointers on sorted lists; intersection is `max(start1, start2)` to `min(end1, end2)` |
| 45 | [Maximum Overlapping Intervals](9.Merge-Intervals/largest_overlap_of_inertavls.py) | Merge Intervals (Sweep Line) | Medium | **Sweep Line** → Sort starts (`+1`) and ends (`-1`); track cumulative sum to find max overlap |
| 46 | [Sum Between Range](10.Prefix_Sum/sum_between_range.py) | Prefix Sum | Easy | **Range Sum** → Precompute prefix sums. `Sum(i, j) = P[j] - P[i-1]`. Handle `i=0`. |
| 47 | [K Sum Subarrays](10.Prefix_Sum/k_sum_sub_array.py) | Prefix Sum (Hash Map) | Medium | **Subarray sum equals K** → Use hash map to store `prefix_sum` frequency; check if `curr_prefix_sum - k` exists in map |
| 48 | [Product of Array Except Self](10.Prefix_Sum/product_array.py) | Prefix & Suffix Products | Medium | **Product without self** → Compute left products in first pass, then multiply by right products in second pass (O(1) space) |
| 49 | [Invert Binary Tree](11.Trees/DFS/1.invert_binary_tree.py) | Trees (DFS) | Easy | **Invert Structure** → Swap left and right children at each node; recurse on both children (DFS) |
| 50 | [Balanced Binary Tree](11.Trees/DFS/2.balanced_bianry_tree.py) | Trees (DFS) | Easy | **Check Balance** → Use DFS to compute height; return -1 if unbalanced; check if `abs(left_height - right_height) > 1` |
| 51 | [Rightmost Nodes of Binary Tree](11.Trees/BFS/1.right_most_nodes.py) | Trees (BFS) | Medium | **Level-order traversal** → Use BFS with queue; track level size, append last node of each level to result |
| 52 | [Widest Binary Tree Level](11.Trees/BFS/2.widest_binary_tree_level.py) | Trees (BFS) | Medium | **Width with gaps** → Use BFS with index tracking `(node, index)`; left child = `2*i+1`, right = `2*i+2`; width = `rightmost - leftmost + 1` |
| 53 | [Validate BST](11.Trees/DFS/3.validate_BST.py) | Trees (DFS) | Medium | **Range validation** → Each node must satisfy `min < node.val < max`; left subtree updates max to `node.val`, right updates min to `node.val` |
| 54 | [Lowest Common Ancestor](11.Trees/DFS/4.LCA.py) | Trees (DFS) | Medium | **LCA in Binary Tree** → If current node is p or q, return it; if both subtrees return non-null, current is LCA; else return non-null subtree result |
| 55 | [Lowest Common Ancestor in BST](11.Trees/DFS/5.LCA_BST.py) | Trees (DFS) | Medium | **Use BST property** → If both p,q < root, go left; if both > root, go right; else root is LCA. O(h) time, O(1) space iterative |
| 56 | [Construct Binary Tree from Preorder and Inorder](11.Trees/DFS/6.build_tree_from_pre_in_order.py) | Trees (DFS) | Medium | **Divide and conquer** → First element in preorder is root; find it in inorder to split left/right subtrees; use hashmap for O(1) lookups |
| 57 | [Binary Tree Maximum Path Sum](11.Trees/DFS/7.maximum_path_sum.py) | Trees (DFS) | Hard | **Max Path Sum** → Track global max (left + root + right); return extendable path to parent (root + max(left, right)) |
| 58 | [Binary Tree Symmetry](11.Trees/DFS/8.binary_tree_symmetry.py) | Trees (DFS) | Easy | **Mirror Structure** → Recursively compare outer pairs and inner pairs; `left.left == right.right` and `left.right == right.left` |
| 59 | [Binary Tree Columns](11.Trees/BFS/3.binary_tree_columns.py) | Trees (BFS) | Medium | **Vertical Order** → BFS with `(node, col)`; track min/max col; collect nodes by column index |
| 60 | [Kth Smallest Element in BST](11.Trees/DFS/9.kth_smallest_element.py) | Trees (DFS) | Medium | **Inorder Property** → Inorder traversal of a BST yields sorted values; stop at the k-th visited node |
| 61 | [Serialize and Deserialize Binary Tree](11.Trees/DFS/10.serialize-deserialize.py) | Trees (DFS) | Hard | **String Encoding** → Preorder DFS for serialization (use `#` for None); use an iterator to deserialize recursively |
| 62 | [Design Trie (Prefix Tree)](12.Tries/design_trie.py) | Tries | Medium | **Prefix Tree** → Use nested dictionaries for children; mark end of word with boolean flag; O(M) for insert/search where M is word length |
| 63 | [Add and Search Word with Wildcards](12.Tries/add_search_word_wildcard.py) | Tries (DFS) | Medium | **Wildcard Search** → Use DFS with recursion when encountering `.` wildcard; explore all children branches; O(M·26^K) worst case where K is wildcards |
| 64 | [Word Search II](12.Tries/find_all_words_on_board.py) | Tries (DFS + Backtracking) | Hard | **Find words on board** → Build Trie from words; DFS from each cell with backtracking; prune Trie branches after finding words. O(M·N·4^L) time |
| 65 | [Clone Graph (Deep Copy)](13.Graphs/1.DFS/1.deep_copy.py) | Graphs (DFS) | Medium | **Clone graph with cycles** → Use DFS with hashmap to track cloned nodes; prevents infinite loops in cyclic graphs. O(V+E) time, O(V) space |
| 66 | [Count Islands](13.Graphs/1.DFS/2.count_islands.py) | Graphs (DFS) | Medium | **Count connected components** → DFS from each unvisited land cell to mark entire island; increment count for each new island found. O(M·N) time |
| 67 | [Matrix Infection (Rotting Oranges)](13.Graphs/2.BFS/1.matrix_infection.py) | Graphs (BFS) | Medium | **Multi-source BFS** → Start BFS from all rotten oranges simultaneously using level-order traversal; track time to infect all fresh oranges. O(M·N) time |
| 68 | [Bipartite Graph Validation](13.Graphs/1.DFS/3.bipartite_graph.py) | Graphs (DFS + 2-Coloring) | Medium | **2-Coloring** → Use DFS to color nodes with 2 colors; if neighbor has same color, graph is not bipartite. Check all components. O(V+E) time |
| 69 | [Longest Increasing Path in Matrix](13.Graphs/1.DFS/4.longest_increasing_path.py) | Graphs (DFS + Memoization) | Hard | **DFS with memo** → From each cell, DFS to neighbors with greater values; cache results to avoid recomputation. O(M·N) time, O(M·N) space |
| 70 | [Word Ladder](13.Graphs/2.BFS/2.word_ladder.py) | Graphs (BFS) | Medium | **Shortest path in implicit graph** → BFS from start; neighbors = one-letter changes; only allow words in dictionary. O(N·L²) time. Optional: bidirectional BFS to meet in the middle |
| 71 | [Merging Communities](13.Graphs/3.Union-Find/merging_communities.py) | Graphs (Union-Find / DSU) | Medium | **Dynamic connectivity** → Use Union-Find with union by size and path compression to keep track of community sizes in near O(1) time |
| 72 | [Course Schedule (Prerequisites)](13.Graphs/4.Topological_Sort/course_schedule.py) | Graphs (Topological Sort / Kahn's Algorithm) | Medium | **Detect cycles in prerequisites** → Build in-degree array and adjacency list; repeatedly take zero in-degree nodes using a queue to check if all courses can be finished |
| 73 | [Connect the Dots (Min Cost to Connect Points)](13.Graphs/3.Union-Find/connect_the_dots.py) | Graphs (MST / Kruskal + Union-Find) | Medium | **Minimum cost to connect all points** → Build all edges with Manhattan distance, sort by cost, and use Kruskal's algorithm with Union-Find to form the MST |
| 74 | [Shortest Path from Source (Dijkstra)](13.Graphs/5.Shortest_Path/dijkstra.py) | Graphs (Dijkstra / Shortest Path) | Medium | **Single-source shortest paths (non-negative edges)** → Use adjacency list with min-heap; relax edges and skip heap entries whose distance is greater than the current best |
| 75 | [Find All Permutations](14.Backtracking/1.Permutation/find_all_permutations.py) | Backtracking | Medium | **All permutations** → Use backtracking with a used set; for each unused element, add to candidate, recurse, then remove (backtrack). O(n × n!) time |
| 76 | [Find All Subsets](14.Backtracking/2.Subset/find_all_subsets.py) | Backtracking | Medium | **All subsets** → For each element, either include or exclude; recurse both ways and backtrack. 2^n subsets. O(n × 2^n) time |
| 77 | [Combination Sum](14.Backtracking/3.Combination/combination_sum.py) | Backtracking | Medium | **Combinations summing to target** → Elements can be reused (pass i, not i+1); backtrack by adding element, recursing, then removing. Exponential time |


> **Note**: This table will be updated as more problems are added to the repository.



## 📝 License

This project is open source and available for educational purposes.

## 🙏 Acknowledgments

- Inspired by common coding interview patterns
- Built for learning and interview preparation


