import heapq
from typing import Counter, List

class Pair:
    def __init__(self, str, freq) -> None:
        self.str = str
        self.freq = freq

    # define a custom comparator
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.str < other.str
        return self.freq > other.freq

# Time - O(n) + k * O(logn), space - O(n)
def k_most_frequent_strings(strs: List[str], k: int) -> List[str]:
    # O(n)
    freqs = Counter(strs)

    # Max-heap heapify - O(n)
    max_heap = [Pair(str, freq) for str, freq in freqs.items()]
    heapq.heapify(max_heap)

    # pop most frequest string from heap k times - k * O(logn)
    return [heapq.heappop(max_heap).str for _ in range(k)]


if __name__ == "__main__":
    strs = ['go', 'coding', 'byte', 'byte', 'go', 'interview', 'go']
    k = 2

    print(k_most_frequent_strings(strs, k))