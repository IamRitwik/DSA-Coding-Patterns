from collections import deque
from typing import List

# Time:  O(N * L^2)  — N = len(dictionary), L = word length.
#       BFS visits each word at most once (O(N) nodes). For each word we try
#       L positions × 26 letters, and each candidate string build + set lookup is O(L).
# Space: O(N * L)   — set(dictionary), queue and visited each hold O(N) words of length L.
def shortest_transformation_sequence(start: str, end: str, dictionary: List[str]) -> int:
    # Write your code here
    dictionary_set = set(dictionary)
    if start not in dictionary_set and end not in dictionary_set:
        return 0
    if start == end:
        return 1
    
    lower_case_alphabet = "abcdefghijklmnopqrstuvwxyz"

    queue = deque([start])
    visited = set([start])
    dist = 0

    while queue:
        for _ in range(len(queue)):
            curr_word = queue.popleft()

            if curr_word == end:
                return dist + 1
            
            for i in range(len(curr_word)):
                for c in lower_case_alphabet:
                    next_word = curr_word[:i] + c + curr_word[i + 1:]
                    
                    if (next_word in dictionary_set and next_word not in visited):
                        visited.add(next_word)
                        queue.append(next_word)
        
        dist += 1
    return 0

def main():
    # Test case 1: Classic word ladder example
    start1 = "hit"
    end1 = "cog"
    dictionary1 = ["hot", "dot", "dog", "lot", "log", "cog"]
    result1 = shortest_transformation_sequence(start1, end1, dictionary1)
    print(f"Test 1: {start1} -> {end1}")
    print(f"Dictionary: {dictionary1}")
    print(f"Shortest transformation sequence length: {result1}")
    print(f"Expected: 5 (hit -> hot -> dot -> dog -> cog)")
    print()

    # Test case 2: No possible transformation
    start2 = "hit"
    end2 = "cog"
    dictionary2 = ["hot", "dot", "dog", "lot", "log"]
    result2 = shortest_transformation_sequence(start2, end2, dictionary2)
    print(f"Test 2: {start2} -> {end2}")
    print(f"Dictionary: {dictionary2}")
    print(f"Shortest transformation sequence length: {result2}")
    print(f"Expected: 0 (no path exists)")
    print()

    # Test case 3: Start and end are the same
    start3 = "hit"
    end3 = "hit"
    dictionary3 = ["hit", "hot", "dot"]
    result3 = shortest_transformation_sequence(start3, end3, dictionary3)
    print(f"Test 3: {start3} -> {end3}")
    print(f"Dictionary: {dictionary3}")
    print(f"Shortest transformation sequence length: {result3}")
    print(f"Expected: 1 (already at target)")
    print()

    # Test case 4: Direct transformation (one step)
    start4 = "hot"
    end4 = "dot"
    dictionary4 = ["hot", "dot", "dog"]
    result4 = shortest_transformation_sequence(start4, end4, dictionary4)
    print(f"Test 4: {start4} -> {end4}")
    print(f"Dictionary: {dictionary4}")
    print(f"Shortest transformation sequence length: {result4}")
    print(f"Expected: 2 (hot -> dot)")

if __name__ == "__main__":
    main()
