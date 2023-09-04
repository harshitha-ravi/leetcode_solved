"""
EASY

Problem --> Given a stones array, where stone[i] is weight of ith stone

Technique
        # Max Heap:
        - implement max heap using min heap - multiply be -1

        - until there's one left - play the game
        - pop two largest
        - if not equal - push new stone
        - append 0 in the ned
        - return the last stone - if not last stone - 0 returned


Goal --> return last stone

Time Complexity : generating heap - O(n)
                  pop - n log n

Companies : Google

"""

import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        """
        Implementing Max Heap:

        - Python doesn't have max heap
        - Need to use min heap, and tweak it

        - what tweaks? - store every elem multiplied by -1
        - so the largest elem will be ta the top (being a smallest)

        - Heads up -> while processing the values, be aware that it's negative
        - and process accordingly

        """

        # generating a max heap, multiplying by -1
        stones = [-i for i in stones]

        # generating max heap
        heapq.heapify(stones)

        # until there's just one stone left, play the game
        while len(stones) > 1:
            # pop the largest two elements
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            # if the weight of the 2 stones is equal - all good, no extra actions required
            # if second < first -> then second is destroyed and,
            # push new stones with weight : first - second (still holds good with -ve values)

            # in this case, as -ve values are stored:
            # second < first is reversed: second > first
            if second > first:
                heapq.heappush(stones, first - second)
                # first - second still holds good, as we want to push the element with -ve sign

        # in the end, if nothing's left in the array, just append 0
        # if any stone is left, it will return that stone
        # else, this appended 0 value is returned
        stones.append(0)

        # return the remaining stone
        return abs(stones[0])


def main():
    solver = Solution()
    print(solver.lastStoneWeight([2, 7, 4, 1, 8, 1]))


if __name__ == "__main__":
    main()
