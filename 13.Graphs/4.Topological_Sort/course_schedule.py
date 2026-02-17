from collections import defaultdict, deque
from typing import List


def prerequisites(n: int, prerequisites: List[List[int]]) -> bool:
    """
    Determine if it is possible to finish all courses given the prerequisites.

    Time Complexity: O(n + m), where n is the number of courses and
    m is the number of prerequisite pairs (edges).
    Space Complexity: O(n + m) for the adjacency list, in-degree array,
    and the queue used in Kahn's algorithm.
    """
    graph = defaultdict(list)
    in_degrees = [0] * n

    # represent the graph as adjacency list
    # record in_degree of each course
    for prereq, course in prerequisites:
        graph[prereq].append(course)
        in_degrees[course] += 1

    Q = deque()

    # add all courses with in_degree of 0 to Q
    for i in range(n):
        if in_degrees[i] == 0:
            Q.append(i)

    enrolled_courses = 0

    # perform topological sort
    while Q:
        node = Q.popleft()
        enrolled_courses += 1
        for neighbor in graph[node]:
            in_degrees[neighbor] -= 1
            # if in_degree of neighbor becomes 0 add to Q
            if in_degrees[neighbor] == 0:
                Q.append(neighbor)

    return enrolled_courses == n


def main() -> None:
    # Example 1: possible to finish all courses
    n = 4
    prereqs = [[0, 1], [1, 2], [2, 3]]  # 0 -> 1 -> 2 -> 3
    print("Can finish all courses (expected True):", prerequisites(n, prereqs))

    # Example 2: not possible due to cycle
    n2 = 2
    prereqs2 = [[0, 1], [1, 0]]  # cycle between 0 and 1
    print("Can finish all courses (expected False):", prerequisites(n2, prereqs2))


if __name__ == "__main__":
    main()
