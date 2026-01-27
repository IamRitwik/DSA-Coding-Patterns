import heapq


class MedianOfAnIntegerStream:
    def __init__(self):
        self.left_half = [] # max heap
        self.right_half = [] # min heap

    # Time - O(logn), space - O(n)
    def add(self, num: int) -> None:
        # if num is <= max of left_half, it belongs to left_half
        if not self.left_half or num <= -self.left_half[0]:
            heapq.heappush(self.left_half, -num)
            # Rebalance if len(left_half) > len(right_half) + 1
            if len(self.left_half) > len(self.right_half) + 1:
                heapq.heappush(self.right_half, -heapq.heappop(self.left_half))
        # otherwise it belongs to right half
        else:
            heapq.heappush(self.right_half, num)
            # Rebalance if len(right_half) > len(left_half)
            if len(self.right_half) > len(self.left_half):
                heapq.heappush(self.left_half, -heapq.heappop(self.right_half))

    # Time - O(1)
    def get_median(self) -> float:
        if len(self.left_half) == len(self.right_half):
            return (-self.left_half[0] + self.right_half[0]) / 2.0
        else:
            return -self.left_half[0]


def main():
    print("Test Case 1: Adding numbers sequentially")
    stream = MedianOfAnIntegerStream()
    numbers = [5, 15, 1, 3, 8, 7, 9, 10]
    
    for num in numbers:
        stream.add(num)
        median = stream.get_median()
        print(f"Added {num}, Current median: {median}")
    
    print("\n" + "="*50 + "\n")
    
    print("Test Case 2: Adding numbers in sorted order")
    stream2 = MedianOfAnIntegerStream()
    numbers2 = [1, 2, 3, 4, 5]
    
    for num in numbers2:
        stream2.add(num)
        median = stream2.get_median()
        print(f"Added {num}, Current median: {median}")
    
    print("\n" + "="*50 + "\n")
    
    print("Test Case 3: Adding numbers in reverse sorted order")
    stream3 = MedianOfAnIntegerStream()
    numbers3 = [10, 8, 6, 4, 2]
    
    for num in numbers3:
        stream3.add(num)
        median = stream3.get_median()
        print(f"Added {num}, Current median: {median}")
    
    print("\n" + "="*50 + "\n")
    
    print("Test Case 4: Adding duplicate numbers")
    stream4 = MedianOfAnIntegerStream()
    numbers4 = [5, 5, 5, 5, 5]
    
    for num in numbers4:
        stream4.add(num)
        median = stream4.get_median()
        print(f"Added {num}, Current median: {median}")
    
    print("\n" + "="*50 + "\n")
    
    print("Test Case 5: Mixed positive and negative numbers")
    stream5 = MedianOfAnIntegerStream()
    numbers5 = [-5, 10, -3, 7, 0, 2]
    
    for num in numbers5:
        stream5.add(num)
        median = stream5.get_median()
        print(f"Added {num}, Current median: {median}")


if __name__ == "__main__":
    main()