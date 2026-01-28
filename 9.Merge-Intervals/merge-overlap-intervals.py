from typing import List

# Definition of Interval:
class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end
    
    def __repr__(self):
        return f"({self.start}, {self.end})"


def merge_overlapping_intervals(intervals: List[Interval]) -> List[Interval]:
    # Time: O(n log n) due to sorting, Space: O(n) for merged output
    intervals.sort(key=lambda x: x.start)

    merged = [intervals[0]]
    
    for B in intervals[1:]:
        A = merged[-1]
        
        # no overlap
        if A.end < B.start:
            merged.append(B)
        else:
            merged[-1] = Interval(A.start, max(A.end, B.end))
    return merged
    


if __name__ == "__main__":
    intervals = [Interval(3, 4), Interval(7, 8), Interval(2, 5), Interval(6, 7), Interval(1, 4)]
    print(intervals)
    print(merge_overlapping_intervals(intervals))