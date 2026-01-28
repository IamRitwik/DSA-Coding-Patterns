from typing import List

# Definition of Interval:
class Interval:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

# Time: O(n log n) due to sorting, Space: O(n)
def largest_overlap_of_intervals(intervals: List[Interval]) -> int:
    # Write your code here
    points = []
    for interval in intervals:
        points.append((interval.start, 'S'))
        points.append((interval.end, 'E'))

    points.sort(key=lambda x: (x[0], x[1]))

    active_intervals = 0
    max_overlaps = 0

    for time, point in points:
        if point == 'S':
            active_intervals += 1
        else:
            active_intervals -= 1
        max_overlaps = max(max_overlaps, active_intervals)
    return max_overlaps

if __name__ == "__main__":
    intervals = [Interval(1, 3), Interval(5, 7), Interval(2, 6), Interval(4, 8)]
    print(largest_overlap_of_intervals(intervals))