from typing import List

# Definition of Interval:
class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

# Time: O(n + m)
# Space: O(1)
def identify_all_interval_overlaps(intervals1: List[Interval], intervals2: List[Interval]) -> List[Interval]:
    # Write your code here
    overlap = []

    i = j = 0

    while i < len(intervals1) and j < len(intervals2):
        if intervals1[i].start <= intervals2[j].start:
            A, B = intervals1[i], intervals2[j]
        else:
            A, B = intervals2[j], intervals1[i]

        if A.end >= B.start:
            overlap.append(Interval(B.start, min(A.end, B.end)))
        
        if intervals1[i].end < intervals2[j].end:
            i += 1
        else:
            j += 1
    return overlap


if __name__ == "__main__":
    # Create lists of Interval objects
    intervals1 = [Interval(1, 4), Interval(5, 6), Interval(9, 10)]
    intervals2 = [Interval(2, 7), Interval(8, 9)]

    overlaps = identify_all_interval_overlaps(intervals1, intervals2)
    # Print overlaps as list of [start, end] for readability
    print([[interval.start, interval.end] for interval in overlaps])