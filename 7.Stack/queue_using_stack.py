"""
Time Complexity Analysis
enqueue(x)
 - O(1)
Simply appends an element to enq_stack
This is a constant time operation
dequeue()
 - Amortized O(1)
Best case: O(1) - when deq_stack has elements, just pop from it
Worst case: O(n) - when deq_stack is empty, all n elements from enq_stack are transferred
Amortized: O(1) - Each element is moved at most once from enq_stack to deq_stack, so over a sequence of operations, the average cost per operation is constant
peek()
 - Amortized O(1)
Same analysis as 
dequeue()
 since it calls 
transer_enq_to_deq()
Best case: O(1)
Worst case: O(n)
Amortized: O(1)
Overall Time Complexity: Amortized O(1) per operation
Space Complexity Analysis
O(n) where n is the number of elements in the queue
"""
class Queue:
    def __init__(self):
        self.enq_stack = []
        self.deq_stack = []

    def enqueue(self, x: int) -> None:
        self.enq_stack.append(x)

    def transer_enq_to_deq(self) -> None:
        # if deq_stack is empty, push all elements from 
        # enq_stack to deq_stack
        if not self.deq_stack:
            while self.enq_stack:
                self.deq_stack.append(self.enq_stack.pop())

    def dequeue(self) -> int:
        self.transer_enq_to_deq()
        return self.deq_stack.pop() if self.deq_stack else None

    def peek(self) -> int:
        self.transer_enq_to_deq()
        return self.deq_stack[-1] if self.deq_stack else None


def main():
    # Create a new queue
    q = Queue()
    
    # Test 1: Enqueue elements
    print("Enqueuing: 1, 2, 3, 4, 5")
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    
    # Test 2: Peek at front element
    print(f"Peek (front element): {q.peek()}")  # Should be 1
    
    # Test 3: Dequeue elements
    print(f"Dequeue: {q.dequeue()}")  # Should be 1
    print(f"Dequeue: {q.dequeue()}")  # Should be 2
    
    # Test 4: Peek after some dequeues
    print(f"Peek (front element): {q.peek()}")  # Should be 3
    
    # Test 5: Enqueue more elements
    print("Enqueuing: 6, 7")
    q.enqueue(6)
    q.enqueue(7)
    
    # Test 6: Dequeue all remaining elements
    print(f"Dequeue: {q.dequeue()}")  # Should be 3
    print(f"Dequeue: {q.dequeue()}")  # Should be 4
    print(f"Dequeue: {q.dequeue()}")  # Should be 5
    print(f"Dequeue: {q.dequeue()}")  # Should be 6
    print(f"Dequeue: {q.dequeue()}")  # Should be 7
    
    # Test 7: Dequeue from empty queue
    print(f"Dequeue from empty queue: {q.dequeue()}")  # Should be None
    print(f"Peek from empty queue: {q.peek()}")  # Should be None


if __name__ == "__main__":
    main()