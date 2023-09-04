"""
EASY - but medium level

Problem --> Given a nums array, and int k, return the Kth largest element, also  need to implement add function - adds new value and
            return Kth largest

Technique
        # Min Heap:

        # Constructor
        # Generate minHeap from array
        # Maintain only k elements: Pop out unwanted elements - heappop

        # Add function:
        # heappush - new value
        # if len > k -> remove unwanted - heappop
        # return top elem minHeap[0]


Goal --> return Kth largest

Time Complexity : add -log n,
                  remove - (n-k) log n

Companies : Amazon

"""


"""
Short Notes on Heap:

What is a heap? :  
- specialized tree-based data structure
- often used to implement priority queues 
- ex: heap-based implementation of Dijkstra's algorithm
- Properties:

Heap Property: (sorted property)
    Max Heap : largest element at root
    Min Heap : smallest element at root
    (any node valye is greater/smaller than it's child nodes)
- Implemented as a binary tree (balanced)

When ? -  efficiently retrieving the min/max element - constant time

Use cases:
 - Priority Queues: elements with higher priority are dequeued before elements with lower priority.
 - Heap Sort: in-place sorting algo - uses binary tree to build sorted array
 - Dijkstra's Algorithm: shortest path algo: min heap
 
Where ? - problems that involve prioritization or sorting.

"""

import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.minHeap, self.k = nums, k

        # Why minHeap for this problem? we are interested in the Kth largest element -
        # That means - we will remove first smaller elements which we are not interested in
        # generate the heap from the given array
        heapq.heapify(self.minHeap)

        # we will just maintain the k elements in our minHeap
        # To do that, remove all the additional elements
        # In minHeap, the min element will be at the top
        # Remove other elements which we are not interested in:
        while len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # In this method we will add an element to the stream i.e. heap
        heapq.heappush(self.minHeap, val)

        # Now, to maintain only th ek elems - pop unwanted
        # we need to pop only when the size is more than k
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # once added - we need to return the kth largest elem (imagine kth from the backwards of array)
        # which is sitting at the top
        return self.minHeap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
