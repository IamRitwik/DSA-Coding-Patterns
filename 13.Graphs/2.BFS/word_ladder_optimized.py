from collections import deque
from typing import Deque, List, Set

# Time:  O(N * L^2)  — Same worst case as one-way BFS (N words, L² per word).
#       Bidirectional search often explores fewer nodes in practice when a path exists.
# Space: O(N * L)   — Two queues and two visited sets, each O(N) words of length L.
def shortest_transformation_sequence(start: str, end: str, dictionary: List[str]) -> int:
    # Include start/end so we can traverse even when they're not in wordList (e.g. LeetCode).
    dictionary_set = set(dictionary) | {start, end}

    if start == end:
        return 1

    start_q = deque([start])
    start_visited: Set[str] = {start}

    end_q = deque([end])
    end_visited: Set[str] = {end}

    level_start = level_end = 0

    while start_q and end_q:
        level_start += 1
        if _explore_level(start_q, start_visited, end_visited, dictionary_set):
            return level_start + level_end + 1
        level_end += 1
        if _explore_level(end_q, end_visited, start_visited, dictionary_set):
            return level_start + level_end + 1
    return 0


def _explore_level(
    queue: Deque[str],
    visited: Set[str],
    other_visited: Set[str],
    dictionary_set: Set[str],
) -> bool:
    """Expand one BFS level; return True if any new node is in other_visited."""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for _ in range(len(queue)):
        curr = queue.popleft()
        for i in range(len(curr)):
            for c in alphabet:
                nxt = curr[:i] + c + curr[i + 1 :]
                if nxt in other_visited:
                    return True
                if nxt in dictionary_set and nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)
    return False