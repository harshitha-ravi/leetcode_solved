"""
MEDIUM

Problem --> Given a stones array, where stone[i] is weight of ith stone

Technique
        # Min Heap:
        3 steps:
        1 - Process and Store in minHeap List - [dist, x, y]
        2 - heapify
        3 - heappop
        4 - return res array


Goal --> return K nearest points

Time Complexity : 1 - Process and store - O(n)
                  2 - heapify - O(n)
                  3 - heappop - k log n

Companies : FACEBOOK

"""

import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        """
        To solve this problem, chunk it out into 3 steps
        Step 1 : Create a list -> minHeap : process the given 2d Array, to calc the distance
                 Store it in the list and append it in the format
                 [distance, x, y] {distance: x ^ 2 + y ^ 2}
                  - no need to find the square root, because we just have to compare
                  - since it's origin - the other co-ord will be (0,0)
        Step 2: Convert the list to heap (heapify)
        Step 3: Based on k -> pop  k elements and append [x,y] to the result list

        """

        # Step 1 - Process and store - O(n)
        minHeap = []

        for x, y in points:
            distance = (x ** 2) + (y ** 2)
            minHeap.append([distance, x, y])

        # Step 2 - Convert the list to heap (heapify) - O(n)
        heapq.heapify(minHeap)

        # Step 3 - Based on k -> pop  k elements and append [x,y] to the result list
        # k log n
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1

        # return res
        return res


def main():
    solver = Solution()
    print(solver.kClosest([[3, 3], [5, -1], [-2, 4]], 2))


if __name__ == "__main__":
    main()
