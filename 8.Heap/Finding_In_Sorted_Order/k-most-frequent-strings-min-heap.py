import heapq
from typing import Counter, List

class Pair:
    def __init__(self, str, freq) -> None:
        self.str = str
        self.freq = freq

    # define a custom comparator
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.str > other.str
        return self.freq < other.freq

# Time - O(n) + O(nlog(k)) + O(klog(k)) + O(k), space - O(n)
def k_most_frequent_strings(strs: List[str], k: int) -> List[str]:
    # O(n)
    freqs = Counter(strs)
    min_heap = []

    for str, freq in freqs.items():
        #O(nlogk)
        heapq.heappush(min_heap, Pair(str, freq))

        if len(min_heap) > k:
            heapq.heappop(min_heap)
    #O(klogk)
    res = [heapq.heappop(min_heap).str for _ in range(k)]
    #O(k)
    res.reverse()

    return res


if __name__ == "__main__":
    strs = ['go', 'coding', 'byte', 'byte', 'go', 'interview', 'go']
    k = 2

    print(k_most_frequent_strings(strs, k))