"""
MEDIUM

Problem --> Koko eating bananas, given an array of piles of bananas, return the min eating speed that finishes eating all piles

Technique --> Binary Search, left and right pointers, keep recalculating mid -> until the target found
          ---> Consider the max no. of bananas as the max speed in the beginning
          --> Then, the speed search space becomes [1...max]
          --> Apply binary search on this speed search space to find the min speed

Goal --> Search min speed

Time Complexity : O( log max(p) . p)

Companies : Google

"""

import math


class Solution:

    def minEatingSpeed(self, piles, h):
        # At first consider that the max eating speed is max no. of bananas in the pile
        # we will do binary search in the space range from 1 ti max speed
        left, right = 1, max(piles)
        minSpeed = max(piles)

        # perform the binary search on the speed space range
        while left <= right:

            # here the mid-value k represents the possible min value speed
            k = (left + right) // 2
            totalTime = 0

            # now that we have the mid-speed, calculate the total hours it takes to eat all the bananas with this speed
            for pile in piles:
                # round up the hours it takes to finish the pile
                totalTime += math.ceil(pile / k)

                # if the hours taken to finish all pile is < given total hours, that will be new min speed
                # And we will continue to explore the possibility of the new min
            if totalTime <= h:
                minSpeed = min(minSpeed, k)
                # shrink the right pointer towards left
                right = k - 1
            else:
                # else, move the left pointer towards right
                left = k + 1

        return minSpeed


def main():
    solver = Solution()
    print(solver.minEatingSpeed([3, 6, 7, 11], 8))


if __name__ == "__main__":
    main()
