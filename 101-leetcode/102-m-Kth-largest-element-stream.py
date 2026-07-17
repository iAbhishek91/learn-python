# Problem: Design a class that tracks the kth largest element in a stream of integers:

# KthLargest(k, nums) — initialize with k and an initial list (may be shorter than k)
# add(val) -> int — insert val, return the current kth largest
# Trace (k = 3, init [4, 5, 8, 2] → heap {4, 5, 8})

# Call Pushed Evicted Heap after Returns
# add(3)3.     3.     {4, 5, 8}.  4
# add(5)5.     4.     {5, 5, 8}.  5
# add(10)10.   5.     {5, 8, 10}. 5
# add(9)9.     5.     {8, 9, 10}. 8
# add(4)4.     4.     {8, 9, 10}. 8
# add(20)20.   8.     {9, 10, 20}. 9
# add(2)2.     2.     {9, 10, 20}. 9
import heapq

class TopKthStream:
    def __init__(self,k: int, nums:list[int]):
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, value:int) -> int:
        heapq.heappushpop(self.min_heap, value)
        return self.min_heap[0]
    
stream = TopKthStream(3, [4, 5, 8, 2])
print(stream.add(3))
print(stream.add(5))
print(stream.add(10))
print(stream.add(9))
print(stream.add(4))
print(stream.add(20))
print(stream.add(2))
